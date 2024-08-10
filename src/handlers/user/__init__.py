from aiogram import Router

from .start import router as start_router

__all__ = (
    "user_router",
)

user_router = Router(name="user_router")
user_router.include_router(start_router)
