from loader import dp
from aiogram.dispatcher.filters import Command
from aiogram import types
from database.loader_db import get_customer


@dp.message_handler(Command('my_profile'))
async def view_profile(message: types.Message):
    customer = get_customer(message.from_user.id)
    await message.answer(f'Your name is {customer.name}\n'
                         f'You live in {customer.city}')
