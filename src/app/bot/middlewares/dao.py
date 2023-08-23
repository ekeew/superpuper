from typing import Callable, Any, Awaitable

import nats
from aiogram import BaseMiddleware
from aiogram.types import TelegramObject
from sqlalchemy.ext.asyncio import async_sessionmaker

from src.app.core import dao


class DatabaseMiddleware(BaseMiddleware):
    def __init__(self, session_pool: async_sessionmaker) -> None:
        self.session_pool = session_pool

    async def __call__(
            self,
            handler: Callable[[TelegramObject, dict[str, Any]], Awaitable[Any]],
            event: TelegramObject,
            data: dict[str, Any]
    ) -> Any:
        async with self.session_pool() as session:
            data["db"] = dao.Database(session)
            return await handler(event, data)


class BrokerMiddleware(BaseMiddleware):
    def __init__(self, nats_dsn: str) -> None:
        self._dsn = nats_dsn

    async def __call__(
            self,
            handler: Callable[[TelegramObject, dict[str, Any]], Awaitable[Any]],
            event: TelegramObject,
            data: dict[str, Any]
    ) -> Any:
        client = await nats.connect([self._dsn])
        data["broker"] = dao.Broker(client)
        result = await handler(event, data)
        await client.close()
        return result
