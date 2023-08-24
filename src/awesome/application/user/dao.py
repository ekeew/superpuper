from abc import ABC, abstractmethod


class BaseUserDAO(ABC):

    @abstractmethod
    async def commit(self) -> None:
        raise NotImplementedError

    @abstractmethod
    async def add_one(self, tid: int) -> bool:
        raise NotImplementedError

    @abstractmethod
    async def get_all_ids(self) -> list[int]:
        raise NotImplementedError
