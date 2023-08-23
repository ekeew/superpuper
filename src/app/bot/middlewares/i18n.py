from typing import Callable, Dict, Any, Awaitable

from aiogram import BaseMiddleware
from aiogram.types import TelegramObject, User
from fluentogram import TranslatorHub


class I18nMiddleware(BaseMiddleware):
    def __init__(self, translator_hub: TranslatorHub) -> None:
        self.hub = translator_hub

    async def __call__(
            self,
            handler: Callable[[TelegramObject, Dict[str, Any]], Awaitable[Any]],
            event: TelegramObject,
            data: Dict[str, Any]
    ) -> Any:
        user: User = data.get("event_from_user")
        data["i18n"] = self.hub.get_translator_by_locale(user.language_code)
        return await handler(event, data)
