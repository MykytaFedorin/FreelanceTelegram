import json
from data.categories import categories_text
from aiogram.dispatcher import FSMContext
from loader import dp
from aiogram.dispatcher.filters import Command
from aiogram import types
from states import Register, WorkerSearch
from database.loader_db import save_customer, get_customer, is_customer_in_db
from keyboards.inline import chose_category_ikb
from keyboards.default import kb_menu, kb_category


@dp.message_handler(text='Find a freelancer', state='*')
async def register_start_text(message: types.Message):
    customer = get_customer(message.from_user.id)
    if customer.id == -1:
        await message.answer('Hello, you have started a registration.\n Enter your name:')
        await Register.name_input.set()
    else:
        await message.answer(text=f'Thank you, {customer.name}.'
                                  f' Choose category you want to find a '
                                  f'freelancer in.', reply_markup=kb_category)
        await WorkerSearch.get_first_level_category.set()


@dp.message_handler(state=Register.name_input)
async def name_input(message: types.Message, state:FSMContext):
    answer = message.text
    await state.update_data(name=answer)
    await message.answer(text='Enter city')
    await Register.city_input.set()


@dp.message_handler(state=Register.city_input)
async def city_input(message: types.Message, state: FSMContext):
    answer = message.text
    await state.update_data(city=answer)
    data = await state.get_data()
    name = data['name']
    city = data['city']
    telegram_id = message.from_user.id
    save_customer(name=name, city=city, telegram_id=telegram_id)
    await message.answer(text=f'Thank you, {name}.\n'
                              f'Your data is saved.', reply_markup=kb_category)
    await message.answer(text=f' Choose category you want to find a '
                              f'freelancer in.', reply_markup=kb_category)
    await state.finish()

