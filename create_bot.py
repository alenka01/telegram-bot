from aiogram import Bot
from aiogram.dispatcher import Dispatcher
import os
from aiogram.contrib.fsm_storage.memory import MemoryStorage

bot = Bot(token=os.getenv('TOKEN'), parse_mode="HTML")
dp=Dispatcher(bot,storage=MemoryStorage())