from aiogram.dispatcher.filters.state import StatesGroup, State


class RegistrationWorker(StatesGroup):
    get_name = State()
    get_first_level_category = State()
    get_second_level_category = State()
    get_description = State()
    get_address = State()
    get_contact = State()
