from aiogram import Router
from aiogram.filters import CommandStart
from aiogram.types import Message
from fluentogram import TranslatorRunner


async def cmd_start(message: Message, i18n: TranslatorRunner) -> None:
    await message.answer(i18n.get("hello"))


def get_common_router() -> Router:
    router = Router()

    router.message.register(cmd_start, CommandStart())

    return router
