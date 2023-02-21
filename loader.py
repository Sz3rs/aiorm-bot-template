from aiogram import Bot, Dispatcher, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from dotenv import load_dotenv
from middlewares import UsersMiddleware
import utils.misc.logging
from os import getenv

load_dotenv()

bot = Bot(token=getenv('botToken'), parse_mode=types.ParseMode.HTML)
storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage)
dp.setup_middleware(UsersMiddleware())
