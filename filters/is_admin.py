from aiogram import types
from aiogram.dispatcher.filters import BoundFilter
from utils.functions import list_admins


class AdminFilter(BoundFilter):
    def __init__(self):
        pass

    async def check(self, message: types.Message):
        return str(message.from_user.id) in list_admins()