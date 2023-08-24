from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from awesome.application.user.dao import BaseUserDAO
from .. import models


class UserDAO(BaseUserDAO):
    def __init__(self, session: AsyncSession) -> None:
        self.session = session

    async def commit(self) -> None:
        await self.session.commit()

    async def add_one(self, tid: int) -> bool:
        if await self.session.get(models.User, tid) is None:
            self.session.add(models.User(tid=tid))
            return True
        return False

    async def get_all_ids(self) -> list[int]:
        return list(await self.session.scalars(select(models.User.tid).limit(None)))
