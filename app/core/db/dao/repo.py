from sqlalchemy.ext.asyncio import AsyncSession

from .user import _UserRepo


class DbRepo:
    def __init__(self, session: AsyncSession) -> None:
        self.session = session
        self.user = _UserRepo(session)

    async def commit(self) -> None:
        await self.session.commit()
