from abc import ABC, abstractmethod
from .user import BaseUser


class BaseDatabase(ABC):
    user: BaseUser

    @abstractmethod
    async def commit(self) -> None:
        raise NotImplementedError
