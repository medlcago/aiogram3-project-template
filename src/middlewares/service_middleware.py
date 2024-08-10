from typing import Callable, Dict, Any, Awaitable

from aiogram import BaseMiddleware
from aiogram.types import CallbackQuery, Message

from core.unitofwork import UnitOfWork
from services import Service


class ServiceMiddleware(BaseMiddleware):
    async def __call__(
            self,
            handler: Callable[[Message | CallbackQuery, Dict[str, Any]], Awaitable[Any]],
            event: Message | CallbackQuery,
            data: Dict[str, Any],
    ) -> Any:
        uow = UnitOfWork()
        data["uow"] = uow
        data["service"] = Service(uow=uow)
        return await handler(event, data)
