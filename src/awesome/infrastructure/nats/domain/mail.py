from dataclasses import dataclass

from nats.aio.msg import Msg

from awesome.application.mailing.domain import BaseMessage


@dataclass
class Message(BaseMessage):
    _msg: Msg

    async def success(self) -> None:
        await self._msg.ack()
