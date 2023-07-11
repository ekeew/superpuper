from typing import Callable, Dict, Any, Awaitable

from aiogram import BaseMiddleware
from aiogram.types import TelegramObject
from sqlalchemy.ext.asyncio import async_sessionmaker

from app.core.db import DbRepo
import nats


class DbMiddleware(BaseMiddleware):
    def __init__(self, session_pool: async_sessionmaker, nats_dsn: str) -> None:
        self.session_pool = session_pool
        self.nats_dsn = nats_dsn

    async def __call__(
            self,
            handler: Callable[[TelegramObject, Dict[str, Any]], Awaitable[Any]],
            event: TelegramObject,
            data: Dict[str, Any]
    ) -> Any:
        async with self.session_pool() as session:
            client = await nats.connect([self.nats_dsn])
            data["db"] = DbRepo(session, client)
            result = await handler(event, data)
            await client.drain()
            return result
