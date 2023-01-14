from aiogram import types
from loader import dp
from data.config import admins_id


@dp.message_handler(text='/setup_bot')
async def setup_bot(message: types.Message):
    if message.from_user.id in admins_id:
        await message.answer(text='Какую функцию вы хотите настроить?')