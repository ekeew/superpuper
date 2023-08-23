from aiogram import Router, F
from aiogram.filters import Command, CommandObject
from aiogram.types import Message
from fluentogram import TranslatorRunner

from src.app.core.config import Settings
from src.app.core.db import DbRepo


async def cmd_send(message: Message, command: CommandObject, db: DbRepo, i18n: TranslatorRunner) -> None:
    for user_id in await db.user.get_all_ids():
        await db.worker.send_message(user_id, command.args)
    await message.answer(i18n.get("success-mailing"))


def get_admin_router() -> Router:
    config = Settings()
    router = Router()

    router.message.register(cmd_send, Command("send", magic=F.args), F.chat.id.in_(config.sender_ids))

    return router
