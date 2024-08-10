from aiogram import Router
from aiogram.filters import CommandStart
from aiogram.types import Message

router = Router(name="start")


@router.message(CommandStart(), flags={"command_start": True})
async def start(message: Message) -> None:
    await message.answer("Hello!")
