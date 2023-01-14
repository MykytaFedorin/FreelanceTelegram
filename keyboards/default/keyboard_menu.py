from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from data import categories_dict, get_subcategories_items
import math


def get_subcat_keyboard(category: str) -> ReplyKeyboardMarkup:
    # function have to return ReplyKeyboardMarkup object,
    # containing right named buttons with subcategories
    # names of category user provide to bot
    items = get_subcategories_items(subcat=category)
    return create_keyboard(items=items)


def create_keyboard(items: list[str]) -> ReplyKeyboardMarkup:
    categories_list = []
    if len(items) < 3:
        row_width = len(items)
    else:
        row_width = 3
    # number_of_rows = len(categories_dict)/3
    row = []
    counter = 1

    for item in items:
        row.append(KeyboardButton(text=item))
        if counter >= row_width:
            counter = 1
            categories_list.append(row)
            row = []
        counter += 1
    categories_list[-1].insert(0, KeyboardButton(text='⬅️ Back to main menu'))
    return ReplyKeyboardMarkup(keyboard=categories_list, resize_keyboard=True)
# for category, subcategory in categories_dict.items():
#     categories_list.append(KeyboardButton(text=category))


kb_menu = ReplyKeyboardMarkup([
    [
        KeyboardButton(text="Find a job"),
        KeyboardButton(text="Find a freelancer"),
    ]
],
    resize_keyboard=True)
kb_category = get_subcat_keyboard(category=categories_dict)

