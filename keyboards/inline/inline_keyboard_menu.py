from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

ikb_menu_start = InlineKeyboardMarkup(row_width=2, inline_keyboard=[
    [
        InlineKeyboardButton(text='Find a freelancer', callback_data='customer'),
        InlineKeyboardButton(text='Find a job', callback_data='freelancer')
    ]
])

chose_category_ikb = InlineKeyboardMarkup(row_width=1, inline_keyboard=[
    [
        InlineKeyboardButton(text='Chose category', callback_data='chose category'),
    ]
])
cancel_registration_ikb = InlineKeyboardMarkup(row_width=1, inline_keyboard=[
    [
        InlineKeyboardButton(text='Cancel', callback_data='cancel registration'),
    ]
])
