from sqlalchemy import String, BigInteger
from sqlalchemy.orm import Mapped, mapped_column

from models.base import Base, TableNameMixin


class User(TableNameMixin, Base):
    user_id: Mapped[int] = mapped_column(BigInteger, unique=True)
    username: Mapped[str | None] = mapped_column(String(128))
