from aiogram.dispatcher.filters.state import StatesGroup, State


class Register(StatesGroup):
    name_input = State()
    city_input = State()
