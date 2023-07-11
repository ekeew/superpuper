from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from ..models import User


class _UserRepo:
    def __init__(self, session: AsyncSession) -> None:
        self.session = session

    async def add(self, tg_id: int) -> bool:
        if await self.session.get(User, tg_id) is None:
            self.session.add(User(tg_id=tg_id))
            return True
        return False

    async def get_all_ids(self) -> list[int]:
        return list(await self.session.scalars(select(User.tg_id).limit(None)))
