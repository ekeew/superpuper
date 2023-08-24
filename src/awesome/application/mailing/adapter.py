from abc import ABC, abstractmethod
from typing import AsyncGenerator, Any

from . import domain


class BaseMailAdapter(ABC):

    @abstractmethod
    async def send_message(self, chat_id: int, text: str) -> None:
        raise NotImplementedError

    @abstractmethod
    @property
    async def messages(self) -> AsyncGenerator[domain.BaseMessage, Any]:
        raise NotImplementedError
