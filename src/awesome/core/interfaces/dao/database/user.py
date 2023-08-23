from abc import ABC, abstractmethod


class BaseUser(ABC):

    @abstractmethod
    async def add(self, tg_id: int) -> bool:
        raise NotImplementedError

    @abstractmethod
    async def get_all_ids(self) -> list[int]:
        raise NotImplementedError
