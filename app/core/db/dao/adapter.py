from sqlalchemy.ext.asyncio import AsyncSession


class DbAdapter:
    def __init__(self, session: AsyncSession) -> None:
        self.session = session

    async def commit(self) -> None:
        await self.session.commit()
