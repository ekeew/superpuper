from abc import ABC, abstractmethod


class BaseDatabase(ABC):

    @abstractmethod
    async def commit(self) -> None:
        raise NotImplementedError
