from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.core.interfaces.dao import BaseUser
from . import models


class User(BaseUser):
    def __init__(self, session: AsyncSession) -> None:
        self.session = session

    async def add(self, tg_id: int) -> bool:
        if await self.session.get(User, tg_id) is None:
            self.session.add(models.User(tg_id=tg_id))
            return True
        return False

    async def get_all_ids(self) -> list[int]:
        return list(await self.session.scalars(select(models.User.tg_id).limit(None)))
