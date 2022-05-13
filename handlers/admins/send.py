from aiogram import types
from aiogram.dispatcher.filters.builtin import Command
from models.user import User
from loader import dp
from models.user import User
from states.send import SendUsers
from filters.is_admin import AdminFilter
from aiogram.dispatcher import FSMContext


@dp.message_handler(AdminFilter(), Command('send'), state='*')
async def bot_start(msg: types.Message, user: User) -> None:
    await SendUsers.waiting_text.set()
    keyboard = types.InlineKeyboardMarkup()
    keyboard.add(types.InlineKeyboardButton('Отмена', callback_data='cancel_send'))
    await msg.answer('Введите текст сообщения:', reply_markup=keyboard)


@dp.callback_query_handler(AdminFilter(), text_contains='cancel_send', state=SendUsers.waiting_text)
async def cancel_send(call: types.CallbackQuery, state=FSMContext) -> None:
    await state.finish()
    await call.message.edit_text('Действие отменено.')


@dp.message_handler(AdminFilter(), content_types=['text'], state=SendUsers.waiting_text)
async def enter_text(msg: types.Message, state: FSMContext):
    await state.update_data(message_for_send=msg)

    keyboard = types.InlineKeyboardMarkup()
    keyboard.add(types.InlineKeyboardButton('Отправить', callback_data='send'))

    await msg.answer('Сохранено! Нажмите, чтобы начать рассылку', reply_markup=keyboard)


@dp.callback_query_handler(AdminFilter(), text_contains='send', state=SendUsers.waiting_text)
async def cancel_send(call: types.CallbackQuery, state=FSMContext) -> None:
    users = User.select().execute()

    await call.message.edit_text(f"Запущено!\n\nКоличество: {len(users)}")

    good = 0
    user_data = await state.get_data()
    message_for_send: types.Message = user_data.get('message_for_send')
    if not message_for_send:
        await state.finish()
        return await call.message.edit_text('Сообщение не найдено')
    await state.finish()

    for user in users:
        try:
            await message_for_send.copy_to(user.id)
            good = good + 1
        except:
            pass

    await call.message.reply(f'Отправлено {good} сообщений!')
