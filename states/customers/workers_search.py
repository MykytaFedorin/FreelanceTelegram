from aiogram.dispatcher.filters.state import StatesGroup, State


class WorkerSearch(StatesGroup):
    get_first_level_category = State()
    get_second_level_category = State()
