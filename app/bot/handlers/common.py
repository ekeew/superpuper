from aiogram import Router
from aiogram.filters import CommandStart
from aiogram.types import Message
from fluentogram import TranslatorRunner

from app.core.db import DbRepo


async def cmd_start(message: Message, db: DbRepo, i18n: TranslatorRunner) -> None:
    if await db.user.add(message.from_user.id):
        await db.commit()
    await message.answer(i18n.get("hello"))


def get_common_router() -> Router:
    router = Router()

    router.message.register(cmd_start, CommandStart())

    return router
