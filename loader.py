from aiogram import Dispatcher, Bot
from data.config import TOKEN
from aiogram.enums import ParseMode


dp = Dispatcher()
bot = Bot(TOKEN, parse_mode=ParseMode.HTML)
