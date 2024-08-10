from typing import TYPE_CHECKING

from .user_service import UserService

if TYPE_CHECKING:
    from core.unitofwork import UnitOfWork


class Service:
    def __init__(self, uow: "UnitOfWork") -> None:
        self.user_service = UserService(uow=uow)
