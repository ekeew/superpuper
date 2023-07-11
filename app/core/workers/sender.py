import asyncio

from aiogram import Bot
from aiogram.exceptions import TelegramRetryAfter
from nats.js import JetStreamContext


async def main(stream: JetStreamContext, bot: Bot) -> None:
    sub = await stream.subscribe("send.messages")
    async for msg in sub.messages:
        chat_id = int(msg.headers.get("chat_id"))
        text = msg.data.decode("utf-8")
        try:
            await bot.send_message(chat_id, text)
            await msg.ack()
        except TelegramRetryAfter as e:
            await asyncio.sleep(e.retry_after)
