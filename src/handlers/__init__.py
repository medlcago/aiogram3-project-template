from aiogram import Dispatcher

from .user import user_router


def register_routes(dp: Dispatcher) -> None:
    dp.include_router(user_router)
