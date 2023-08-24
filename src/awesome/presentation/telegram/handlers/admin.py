from aiogram import Router, F
from aiogram.filters import Command, CommandObject
from aiogram.types import Message
from fluentogram import TranslatorRunner

from awesome.core.config import Settings
from awesome.core.interfaces import dao, adapters


async def cmd_send(
        message: Message,
        command: CommandObject,
        database: dao.BaseDatabase,
        broker: adapters.BaseBroker,
        i18n: TranslatorRunner
) -> None:
    for user_id in await database.user.get_all_ids():
        await broker.mailing.send_message(user_id, command.args)
    await message.answer(i18n.get("success-mailing"))


def get_admin_router() -> Router:
    config = Settings()
    router = Router()

    router.message.register(cmd_send, Command("send", magic=F.args), F.chat.id.in_(config.sender_ids))

    return router
