from typing import AsyncGenerator, Any

from nats import NATS

from awesome.application.mailing.adapter import BaseMailAdapter
from ..domain.mail import BaseMessage


class MailAdapter(BaseMailAdapter):
    def __init__(self, client: NATS) -> None:
        self.client = client
        self.stream = client.jetstream()

    async def send_message(self, chat_id: int, text: str) -> None:
        await self.stream.publish("send.messages", text.encode("utf-8"), headers={"chat_id": str(chat_id)})

    @property
    async def messages(self) -> AsyncGenerator[BaseMessage, Any]:
        sub = await self.stream.subscribe("send.messages")
        async for message in sub.messages:
            yield message
