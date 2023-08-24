import asyncio

from aiogram import Bot
from aiogram.exceptions import TelegramRetryAfter, TelegramForbiddenError

from . import adapter


class Mailing:
    def __init__(self, bot: Bot, mail_adapter: adapter.BaseMailAdapter) -> None:
        self.bot = bot
        self.adapter = mail_adapter

    async def add_mails(self, text: str, chat_ids: list[int]) -> None:
        for chat_id in chat_ids:
            await self.adapter.send_message(chat_id, text)

    async def send_mails(self) -> None:
        async for message in self.adapter.messages:  # type: ignore
            try:
                await self.bot.send_message(message.chat_id, message.text)
                await message.success()
            except TelegramRetryAfter as e:
                await asyncio.sleep(e.retry_after)
            except TelegramForbiddenError:
                pass
