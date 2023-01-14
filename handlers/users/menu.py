from loader import dp
from aiogram import types
from aiogram.dispatcher.filters import Command
from keyboards.default import kb_menu

@dp.message_handler(Command(commands=["menu"], prefixes=['/']))
async def menu(message: types.Message):
    await message.answer(text="Choose an option from list below", reply_markup=kb_menu)