from abc import ABC


class BaseMailing(ABC):

    async def send_message(self, chat_id: int, text: str) -> None:
        raise NotImplementedError
