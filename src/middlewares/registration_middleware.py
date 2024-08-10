from typing import Any, Callable, Dict, Awaitable

from aiogram import BaseMiddleware
from aiogram.dispatcher.flags import get_flag
from aiogram.types import Message

from services import Service


class RegistrationMiddleware(BaseMiddleware):
    async def __call__(
            self,
            handler: Callable[[Message, Dict[str, Any]], Awaitable[Any]],
            event: Message,
            data: Dict[str, Any]
    ) -> Any:
        command_start = get_flag(data, "command_start")
        if not command_start:
            return await handler(event, data)

        user_id = event.from_user.id
        service: Service = data.get("service")
        exists = await service.user_service.get_user(user_id=user_id)
        if exists:
            return await handler(event, data)
        user = await service.user_service.register_user(user=event.from_user)
        data["user"] = user
        return await handler(event, data)
