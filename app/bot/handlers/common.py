from aiogram import Router
from aiogram.filters import CommandStart
from aiogram.types import Message


async def cmd_start(message: Message) -> None:
    await message.answer("Hello World!")


def get_common_router() -> Router:
    router = Router()

    router.message.register(cmd_start, CommandStart())

    return router
