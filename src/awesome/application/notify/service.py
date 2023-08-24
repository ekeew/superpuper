import logging
from contextlib import suppress

from aiogram import Bot
from aiogram.exceptions import TelegramForbiddenError
from taskiq import TaskiqScheduler, TaskiqEvents, TaskiqState, Context, TaskiqDepends
from taskiq.schedule_sources import LabelScheduleSource
from taskiq_nats import NatsBroker

from awesome.infrastructure.config import Settings

config = Settings()
broker = NatsBroker(config.nats.dsn, queue="notifying")
scheduler = TaskiqScheduler(broker, [LabelScheduleSource(broker)])


@broker.on_event(TaskiqEvents.WORKER_STARTUP)
async def startup(state: TaskiqState) -> None:
    logging.basicConfig(
        level=logging.INFO,
        format="%(levelname)-8s [%(asctime)s] :: %(name)s : %(message)s"
    )
    logger = logging.getLogger(__name__)
    logger.warning("Starting scheduler...")

    bot = Bot(config.bot.token.get_secret_value())

    state.bot = bot
    state.admin_id = config.admin_id
    state.logger = logger


@broker.on_event(TaskiqEvents.WORKER_SHUTDOWN)
async def shutdown(state: TaskiqState) -> None:
    await state.bot.session.close()
    state.logger.warning("Scheduler stopped")


@broker.task(task_name="notify", schedule=[{"cron": "*/1 * * * *"}])
async def notify(context: Context = TaskiqDepends()) -> None:
    bot: Bot = context.state.bot
    admin_id: int = context.state.admin_id
    with suppress(TelegramForbiddenError):
        await bot.send_message(admin_id, "12 часов! пора какать")
