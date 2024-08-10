from sqlalchemy import MetaData
from sqlalchemy.orm import DeclarativeBase, declared_attr, Mapped, mapped_column

from core.settings import settings


class Base(DeclarativeBase):
    __abstract__ = True

    id: Mapped[int] = mapped_column(primary_key=True)

    metadata = MetaData(
        naming_convention=settings.db.naming_convention
    )

    def __repr__(self) -> str:
        package = self.__class__.__module__
        class_ = self.__class__.__name__
        attrs = ((k, getattr(self, k)) for k in self.__mapper__.columns.keys())
        sattrs = ', '.join(f'{key}={value!r}' for key, value in attrs)
        return f'{package}.{class_}({sattrs})'


class TableNameMixin:
    @declared_attr.directive
    def __tablename__(cls) -> str:
        return f"{cls.__name__.lower()}s"
