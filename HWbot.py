from aiogram.utils import executor
from create_bot import dp
from Handlers import handler
from DataBase import home_work_db


async def on_startup(_):
    print("Bot is online")
    home_work_db.sql_start()


handler.register_handlers(dp)
executor.start_polling(dp, skip_updates=True, on_startup=on_startup)

