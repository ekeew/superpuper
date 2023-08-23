import asyncio
import logging

import nats
from aiogram import Bot, Dispatcher
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker

from awesome.present.telegram.handlers import get_main_router
from awesome.present.telegram.middlewares import I18nMiddleware, DatabaseMiddleware, BrokerMiddleware
from awesome.present.telegram.translation import get_translator_hub
from awesome.services import mailing
from awesome.core.config import Settings


async def main() -> None:
    logging.basicConfig(
        level=logging.INFO,
        format="%(levelname)-8s [%(asctime)s] :: %(name)s : %(message)s"
    )
    logger = logging.getLogger(__name__)

    config = Settings()

    bot = Bot(token=config.bot.token.get_secret_value())
    dp = Dispatcher()

    engine = create_async_engine(config.postgres.dsn)
    session_pool = async_sessionmaker(engine, expire_on_commit=False)

    client = await nats.connect([config.nats.dsn])
    stream = client.jetstream()

    dp.include_router(get_main_router())
    dp.update.middleware(I18nMiddleware(get_translator_hub(config.project_dir)))
    dp.update.middleware(DatabaseMiddleware(session_pool))
    dp.update.middleware(BrokerMiddleware(config.nats.dsn))

    try:
        logger.warning("Running telegram")
        await asyncio.gather(
            dp.start_polling(bot),
            mailing.main(stream, bot)
        )
    finally:
        await client.drain()
        await dp.storage.close()
        logger.warning("Bot stopped")


if __name__ == "__main__":
    try:
        asyncio.run(main())
    except (KeyboardInterrupt, SystemExit):
        pass