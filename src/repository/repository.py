from typing import Optional

from sqlalchemy import update, select
from sqlalchemy.ext.asyncio import AsyncSession


class Repository[T]:
    model: type[T] = None

    def __init__(self, session: AsyncSession) -> None:
        self.session = session

    async def create(self, **kwargs) -> T:
        instance = self.model(**kwargs)
        self.session.add(instance)
        return instance

    async def get(self, _id: int) -> Optional[T]:
        return await self.session.get(self.model, _id)

    async def filter_by(self, **kwargs) -> Optional[T]:
        stmt = select(self.model).filter_by(**kwargs)
        return await self.session.scalar(stmt)

    async def update(self, _id: int, **kwargs) -> Optional[T]:
        stmt = update(self.model).filter_by(id=_id).values(**kwargs).returning(self.model)
        return await self.session.scalar(stmt)

    async def delete(self, instance: T) -> None:
        await self.session.delete(instance)
