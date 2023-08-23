from abc import ABC


class BaseUser(ABC):

    async def add(self, tg_id: int) -> bool:
        raise NotImplementedError

    async def get_all_ids(self) -> list[int]:
        raise NotImplementedError
