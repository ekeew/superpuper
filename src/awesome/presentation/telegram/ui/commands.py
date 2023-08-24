from aiogram.types import BotCommand
from fluentogram import TranslatorRunner


def get_default_commands(i18n: TranslatorRunner) -> list[BotCommand]:
    return [
        BotCommand(command="hello", description=i18n.get("cmd-hello"))
    ]
