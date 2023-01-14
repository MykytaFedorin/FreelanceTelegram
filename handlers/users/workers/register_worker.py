from aiogram.dispatcher import FSMContext

from data import categories_dict
from database.loader_db import save_worker, find_worker, is_worker_in_db
from keyboards import get_subcat_keyboard
from loader import dp
from aiogram.dispatcher.filters import Command
from aiogram import types
from states import RegistrationWorker
from loader import bot
from keyboards.default import kb_category

cancel_text = 'Registration was canceled'


@dp.message_handler(text='Find a job')
async def register_worker(message: types.Message):
    if not is_worker_in_db(telegram_id=message.from_user.id):
        await message.answer(text="Hello, dear stranger.\n"
                                  "Let's start the registration!")
        await message.answer(text="Enter you full name, please.")
        await RegistrationWorker.get_name.set()
    else:
        await message.answer(text="I'll notify you, when customers appear.")


@dp.message_handler(state=RegistrationWorker.get_name)
async def get_workers_name(message: types.Message, state: FSMContext):
    name = message.text
    await state.update_data(name=name)
    await message.answer(text="Ok, now let me know your \n"
                              "category you want to work in.)", reply_markup=kb_category)
    await RegistrationWorker.get_first_level_category.set()


@dp.message_handler(state=RegistrationWorker.get_first_level_category)
async def get_workers_first_category(message: types.Message, state: FSMContext):
    chosen_category = message.text
    await state.update_data(first_level_category=chosen_category)
    subcategory = categories_dict.get(chosen_category)
    if subcategory:
        keyboard = get_subcat_keyboard(category=subcategory)
        await message.answer(text=f'Please, chose one of the subcategories from menu.', reply_markup=keyboard)
        await RegistrationWorker.get_second_level_category.set()


@dp.message_handler(state=RegistrationWorker.get_second_level_category)
async def get_second_level_category(message: types.Message, state: FSMContext):
    chosen_subcat = message.text
    state_data_dict = await state.get_data()
    first_level_cat = state_data_dict['first_level_category']
    full_category_path = first_level_cat + '/' + chosen_subcat
    await state.update_data(category=full_category_path)
    await message.answer(text="Awesome, now let's describe yourself for your future customers.")
    await RegistrationWorker.get_description.set()


@dp.message_handler(state=RegistrationWorker.get_description)
async def get_workers_description(message: types.Message, state: FSMContext):
    description = message.text
    await state.update_data(description=description)
    await message.answer(text="Awesome, now I have to \n"
                              "ask you for your address.")
    await RegistrationWorker.get_address.set()


@dp.message_handler(state=RegistrationWorker.get_address)
async def get_workers_address(message: types.Message, state: FSMContext):
    address = message.text
    await state.update_data(address=address)
    await message.answer(text="We've almost finished,\n"
                              "Enter your Facebook or Instagram link.")
    await RegistrationWorker.get_contact.set()


@dp.message_handler(state=RegistrationWorker.get_contact)
async def get_workers_contact(message: types.Message, state: FSMContext):
    contact = message.text
    await state.update_data(contact=contact)
    data = await state.get_data()
    save_worker(telegram_id=message.from_user.id,
                name=data['name'],
                category=data['category'],
                description=data['description'],
                address=data['address'],
                contact=data['contact'])
    await message.answer(text=f"Good job,{data['name']}. \n"
                              f"You will work in {data['category']},"
                              f"Now it's time to wait for your\n"
                              f"first customer.")
    await state.finish()
