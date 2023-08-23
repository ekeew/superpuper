from aiogram import Router, Bot
from aiogram.filters import Command
from aiogram.types import Message, BotCommandScopeChat
from fluentogram import TranslatorRunner

from src.app.core.interfaces import dao
from ..ui import get_default_commands


async def cmd_start(message: Message, bot: Bot, database: dao.BaseDatabase, i18n: TranslatorRunner) -> None:
    if await database.user.add(message.from_user.id):
        await database.commit()
        scope = BotCommandScopeChat(chat_id=message.chat.id)
        await bot.set_my_commands(get_default_commands(i18n), scope)

    await message.answer(i18n.get("hello"))


async def cmd_hello(message: Message, i18n: TranslatorRunner) -> None:
    await message.answer(i18n.get("hello"))


def get_common_router() -> Router:
    router = Router()

    router.message.register(cmd_start, Command("start"))
    router.message.register(cmd_hello, Command("hello"))

    return router
