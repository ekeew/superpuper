from sqlalchemy.ext.asyncio import AsyncSession

from app.core.interfaces.dao import BaseDatabase
from .user import User


class PostgresDb(BaseDatabase):
    def __init__(self, session: AsyncSession) -> None:
        self.session = session
        self.user = User(session)

    async def commit(self) -> None:
        await self.session.commit()
