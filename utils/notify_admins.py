import logging
from aiogram import Dispatcher
from data.config import admins_id

async def on_startup_notify(dp: Dispatcher):
    message = "Bot is up!"
    for admin in admins_id:
        try:
            await dp.bot.send_message(chat_id=admin, text=message)
        except Exception as ex:
            logging.exception(ex)