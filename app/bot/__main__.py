import asyncio
import logging

from aiogram import Bot, Dispatcher

from app.core.config import Settings
from .handlers import get_main_router
from .translation import get_translator_hub
from .middlewares import I18nMiddleware


async def main() -> None:
    logging.basicConfig(
        level=logging.INFO,
        format="%(levelname)-8s [%(asctime)s] :: %(name)s : %(message)s"
    )
    logger = logging.getLogger(__name__)

    config = Settings()

    bot = Bot(token=config.bot.token.get_secret_value())
    dp = Dispatcher()

    dp.include_router(get_main_router())
    dp.update.middleware(I18nMiddleware(get_translator_hub()))

    try:
        logger.warning("Running bot")
        await dp.start_polling(bot, allowed_updates=dp.resolve_used_update_types())
    finally:
        await dp.storage.close()
        logger.warning("Bot stopped")


if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        pass
