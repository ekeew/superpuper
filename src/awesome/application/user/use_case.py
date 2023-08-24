import asyncio

from awesome.application.mailing import Mailing
from . import dao


class User:
    def __init__(self, user_dao: dao.BaseUserDAO, mailing: Mailing) -> None:
        self.dao = user_dao
        self.mailing = mailing

    async def add_one(self, tid: int) -> bool:
        if result := await self.dao.add_one(tid):
            await self.dao.commit()
        return result

    async def send_mails(self, text: str) -> None:
        user_ids = await self.dao.get_all_ids()
        await asyncio.create_task(self.mailing.add_mails(user_ids, text))
