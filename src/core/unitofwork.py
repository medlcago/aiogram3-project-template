from core.db import db_helper
from repository import UserRepository


class UnitOfWork:
    def __init__(self):
        self.session_factory = db_helper.session_factory

    async def __aenter__(self):
        self.session = self.session_factory()
        self.user_repository = UserRepository(session=self.session)

    async def __aexit__(self, exc_type, exc_value, traceback):
        if exc_type is None:
            await self.commit()
        else:
            await self.rollback()
        await self.close()

    async def commit(self):
        await self.session.commit()

    async def rollback(self):
        await self.session.rollback()

    async def close(self):
        await self.session.close()
