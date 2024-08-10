from aiogram import Dispatcher

from .registration_middleware import RegistrationMiddleware
from .service_middleware import ServiceMiddleware


def register_global_middlewares(dp: Dispatcher) -> None:
    dp.message.middleware(RegistrationMiddleware())
    dp.callback_query.middleware(RegistrationMiddleware())

    dp.message.outer_middleware(ServiceMiddleware())
    dp.callback_query.outer_middleware(ServiceMiddleware())
