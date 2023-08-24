from abc import ABC, abstractmethod
from dataclasses import dataclass


@dataclass
class BaseMessage(ABC):
    chat_id: int
    text: str

    @abstractmethod
    async def success(self) -> None:
        raise NotImplementedError
