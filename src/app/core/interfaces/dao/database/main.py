from abc import ABC


class BaseDatabase(ABC):
    async def commit(self) -> None:
        raise NotImplementedError
