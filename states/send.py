from aiogram.dispatcher.filters.state import State, StatesGroup


class SendUsers(StatesGroup):
    waiting_text = State()
