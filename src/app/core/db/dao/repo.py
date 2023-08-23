from nats import NATS
from sqlalchemy.ext.asyncio import AsyncSession

from .user import _UserRepo
from .worker import _WorkerRepo


class DbRepo:
    def __init__(self, session: AsyncSession, client: NATS) -> None:
        self.session = session
        self.client = client
        self.user = _UserRepo(session)
        self.worker = _WorkerRepo(client)

    async def commit(self) -> None:
        await self.session.commit()
