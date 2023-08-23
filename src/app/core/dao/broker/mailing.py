from nats import NATS

from app.core.interfaces.dao import BaseMailing


class Mailing(BaseMailing):
    def __init__(self, client: NATS) -> None:
        self.client = client
        self.stream = client.jetstream()

    async def send_message(self, chat_id: int, text: str) -> None:
        await self.stream.publish("send.messages", text.encode("utf-8"), headers={"chat_id": str(chat_id)})