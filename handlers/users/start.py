from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart
from models.user import User
from loader import dp


@dp.message_handler(CommandStart())
async def bot_start(msg: types.Message, user: User) -> None:
    print(user.id)
    await msg.answer(f"👋 Привет, {msg.from_user.first_name}")
