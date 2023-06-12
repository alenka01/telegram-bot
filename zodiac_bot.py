from aiogram.utils import executor 
from create_bot import dp
from aiogram import types
from database import zodiacDB


async def on_startup(_):
    print('Бот вышел в онлайн')
    zodiacDB.sql_start()



from handlers import client

client.register_handlers_client(dp)

@dp.message_handler()
async def empty(message : types.Message):
    await message.answer('Я не понимаю тебя, давай лучше обратимся к команде /help')


executor.start_polling(dp, skip_updates=True, on_startup=on_startup)