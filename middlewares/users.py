from aiogram.dispatcher.middlewares import BaseMiddleware
from aiogram.dispatcher.handler import SkipHandler
from aiogram import types
from models.user import User, DoesNotExist


class UsersMiddleware(BaseMiddleware):
    def __init__(self) -> None:
        super(UsersMiddleware, self).__init__()

    async def on_pre_process_message(self, message: types.Message, data: dict):
        user_id = message.from_user.id

        try:
            user = User.get(id=user_id)
        except DoesNotExist:
            user = User.create(id=user_id)
            user.username = message.from_user.username
            user.save()

        data['user'] = user

    async def on_pre_process_callback_query(self, call: types.CallbackQuery, data: dict):
        user_id = call.from_user.id

        try:
            user = User.get(id=user_id)
        except DoesNotExist:
            user = User.create(id=user_id)
            user.username = call.from_user.username
            user.save()

        data['user'] = user
