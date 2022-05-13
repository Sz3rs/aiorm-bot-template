from aiogram import types
from aiogram.dispatcher.filters.builtin import Command
from models.user import User
from loader import dp
from filters.is_admin import AdminFilter
from aiogram.dispatcher import FSMContext


@dp.message_handler(AdminFilter(), Command('stat'), state='*')
async def bot_start(msg: types.Message, user: User, state: FSMContext) -> None:
    users_count = User.select().count()
    await msg.answer(f'Всего пользователей: {users_count}')
