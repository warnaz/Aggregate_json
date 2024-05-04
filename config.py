import os
from dotenv import load_dotenv
from aiogram import Bot, Dispatcher


load_dotenv()

bot = Bot(token=os.getenv("BOT_TOKEN"))
dp = Dispatcher(bot=bot)

valid_formats = {"dt_from": "", "dt_upto": "", "group_type": "month"}
