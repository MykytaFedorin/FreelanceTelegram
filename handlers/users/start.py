from aiogram import types
from loader import dp
from keyboards.default import kb_menu
from loader import bot


@dp.message_handler(text='/start')
async def command_start(message: types.Message):
    await message.answer(f'Hi, nice to meet you!🖐\nChoose the problem in menu I could help you with. \n', reply_markup=kb_menu)
