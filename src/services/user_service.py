from typing import TYPE_CHECKING, Optional

if TYPE_CHECKING:
    from core.unitofwork import UnitOfWork
    from aiogram.types import User as UserType
    from models import User


class UserService:
    def __init__(self, uow: "UnitOfWork") -> None:
        self.uow = uow

    async def register_user(self, user: "UserType") -> "User":
        async with self.uow:
            user = await self.uow.user_repository.create(
                user_id=user.id,
                username=user.username,
            )
            return user

    async def get_user(self, user_id: int) -> Optional["User"]:
        async with self.uow:
            user = await self.uow.user_repository.filter_by(user_id=user_id)
            return user
