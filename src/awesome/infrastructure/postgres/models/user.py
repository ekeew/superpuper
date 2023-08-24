from sqlalchemy.dialects.postgresql import BIGINT
from sqlalchemy.orm import Mapped, mapped_column

from awesome.application.user import dto
from .base import Base


class User(Base):
    __tablename__ = "users"

    tid: Mapped[int] = mapped_column(BIGINT, primary_key=True, autoincrement=False)

    def as_dto(self) -> dto.User:
        return dto.User(
            tid=self.tid
        )
