from aiogram import types
from aiogram.dispatcher import FSMContext
from database.loader_db import Worker
from database.loader_db import find_worker
from loader import dp
from states import WorkerSearch
from aiogram.dispatcher.filters import Command
from data import categories_dict
from keyboards.default import kb_menu
from data import categories_dict
from keyboards import get_subcat_keyboard


@dp.message_handler(text='⬅️ Back to main menu', state="*")
async def back_to_main_menu(message: types.Message, state: FSMContext):
    await message.answer(text='Choose your option, please.', reply_markup=kb_menu)
    await state.finish()


@dp.message_handler(state=WorkerSearch.get_first_level_category)
async def get_first_level_category(message: types.Message, state: FSMContext):
    chosen_category = message.text
    await state.update_data(first_level_category=chosen_category)
    subcategory = categories_dict.get(chosen_category)
    if subcategory:
        keyboard = get_subcat_keyboard(category=subcategory)
        await message.answer(text=f'Please, chose one of the subcategories from menu.', reply_markup=keyboard)
        await WorkerSearch.get_second_level_category.set()


@dp.message_handler(state=WorkerSearch.get_second_level_category)
async def get_second_level_category(message: types.Message, state: FSMContext):
    chosen_subcat = message.text
    state_data_dict = await state.get_data()
    first_level_cat = state_data_dict['first_level_category']
    full_category_path = first_level_cat + '/' + chosen_subcat
    workers = find_worker(full_category_path)
    for worker in workers:
        await message.answer(text=f"Name: {worker.name}\n"
                                  f"Category: {worker.category}\n"
                                  f"Description: {worker.description}\n"
                                  f"Address: {worker.address}\n"
                                  f"Contact: {worker.contact}")
