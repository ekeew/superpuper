import asyncio
import logging
from pathlib import Path

import nats
from aiogram import Bot, Dispatcher
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker

from app.core.config import Settings
from app.core.workers import mailing
from .handlers import get_main_router
from .middlewares import I18nMiddleware, DbMiddleware
from .translation import get_translator_hub


async def main() -> None:
    logging.basicConfig(
        level=logging.INFO,
        format="%(levelname)-8s [%(asctime)s] :: %(name)s : %(message)s"
    )
    logger = logging.getLogger(__name__)

    project_dir = Path(__file__).parent.parent.parent
    config = Settings()

    bot = Bot(token=config.bot.token.get_secret_value())
    dp = Dispatcher()

    engine = create_async_engine(config.postgres.dsn)
    session_pool = async_sessionmaker(engine, expire_on_commit=False)

    client = await nats.connect([config.nats.dsn])
    stream = client.jetstream()

    dp.include_router(get_main_router())
    dp.update.middleware(I18nMiddleware(get_translator_hub(project_dir)))
    dp.update.middleware(DbMiddleware(session_pool, config.nats.dsn))

    try:
        logger.warning("Running bot")
        await asyncio.gather(
            dp.start_polling(bot, allowed_updates=dp.resolve_used_update_types()),
            mailing.main(stream, bot)
        )
    finally:
        await client.drain()
        await dp.storage.close()
        logger.warning("Bot stopped")


if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        pass
