import asyncio
import logging

from aiogram import Bot, Dispatcher
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker

from awesome.infrastructure.config import Settings
from awesome.presentation.telegram.handlers import get_main_router
from awesome.presentation.telegram.middlewares import I18nMiddleware, DatabaseMiddleware, BrokerMiddleware
from awesome.presentation.telegram.translation import get_translator_hub


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

    dp.include_router(get_main_router())
    dp.update.middleware(I18nMiddleware(get_translator_hub(config.project_dir)))
    dp.update.middleware(DatabaseMiddleware(session_pool))
    dp.update.middleware(BrokerMiddleware(config.nats.dsn))

    try:
        logger.warning("Bot started")
        await dp.start_polling(bot)
    finally:
        await dp.storage.close()
        logger.warning("Bot stopped")


if __name__ == "__main__":
    try:
        asyncio.run(main())
    except (KeyboardInterrupt, SystemExit):
        pass
