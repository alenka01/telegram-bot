from aiogram.dispatcher import FSMContext
from aiogram import types, Dispatcher
from create_bot import dp, bot
from keyboards import ini_client, ini_year, ini_client_url, ini_yearclient_url
from database import zodiacDB
from aiogram.dispatcher.filters import Text
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.dispatcher.filters.state import State,StatesGroup
from aiogram.contrib.fsm_storage.memory import MemoryStorage
import requests
from bs4 import BeautifulSoup

async def message_start(message : types.Message):
    try:
        await message.answer('<b>Привет!</b>✋\n Я <i>Telegram-бот</i>👾 созданный для твоего <i>развлечения</i>)\nУ меня ты сможешь:\n<b>*</b>Найти краткое <b>описание</b> всех <b>знаков зодиака</b>✅\n<b>*</b>Посчитать свою <b>натальную карту</b><s>(что это и зачем есть в справочной информации)</s>✅\n<b>*</b>Посмотреть свой <b>гороскоп</b>✅\n<b>*</b>Узнать свое <b>предсказание дня!</b>✅\n\n<b>Для полного ознакомления с моими возможностями нажми на</b> /help💡\nДля ввода команд нажми на <b><i>меню</i></b>👇')
    except:
        await message.reply('Общение с ботом только в личных сообщениях, напишите ему:\nhttps://t.me/ForYourZodiacbot')
    finally:
        return
 
# @dp.message_handler(commands=['help'])
async def commands_start(message : types.Message):
    try:
        await bot.send_message(message.from_user.id, '<b>Добро пожаловать!</b>✋\n\nВот список команд, которые <i>YourZodiac</i>-bot может выполнить:\n\n/reg - Зарегистрируйтесь, так мы будем лучше знать о нашей аудитории, чтобы развивать проект\n\n/drop - Удаление информации из базы данных о пользователе\
                               \n\n/zodiac - Описание каждого знака зодиака\n\n/china_zodiac - Описание каждого китайского знака зодиака\n\n/horoscope - Гороскоп на день для обычных знаков зодиака\n\n/year_horoscope - Гороскоп на день для китайских знаков зодиака\
                               \n\n/karta - Посчитать натальную карту*.\n\n<b>*</b>\n<b>Что такое натальная карта?</b>Натальная карта(ее также называют космограмма или личный гороскоп рождения) - это своего рода диаграмма, составленная с учетом положения небесных тел в момент вашего рождения. С помощью неё можно узнать какие ещё знаки зодиака влияют на жизнь и характер.\n\n/prediction - Я тебе сам сгенерирую твое предсказание на день\n\n/review - Оставьте отзыв, если хотите развить этот проект\n\n❗Если ты уже оставлял <i>отзыв</i>, то нажми на команду <b>/update</b> для очистки данных и знаво проголосуй')
        await message.delete()
    except:
        await message.reply('Общение с ботом только в личных сообщениях, напишите ему:\nhttps://t.me/ForYourZodiacbot')
    finally:
        return
    
@dp.callback_query_handler(lambda x: x.data and x.data.startswith('del '))
async def push_inline(callback_query : types.CallbackQuery):
     read= await zodiacDB.sql_read(callback_query.data.replace('del ',''))
     for ink in read:
          await callback_query.message.answer(f'<b><i>{ink[1]}</i></b>\n<b>Начало периода</b>: {ink[2]}\n<b>Конец периода:</b> {ink[3]}\n<b>Описание</b>\n {ink[4]}')
     await callback_query.message.answer(f'<b>Заинтересовало?</b>\nДля детального ознакомления можешь перейти по <b><a href="https://www.infoorel.ru/public/public_echo.php?id=1119">cсылке</a></b>', disable_web_page_preview=True)
     await callback_query.message.answer(f'<i>Понравилось?</i>😊\n\nДля продолжения работы с ботом впишите необходимую вам функцию в строку\n\n<b>Для дальнейшей работы с ботом нажмите на меню👇</b>', disable_web_page_preview=True)
     await callback_query.answer()
     await bot.edit_message_reply_markup(
        chat_id=callback_query.from_user.id,
        message_id=callback_query.message.message_id, 
        reply_markup=None
    )
     await bot.delete_message(chat_id=callback_query.from_user.id, message_id=callback_query.message.message_id)

@dp.callback_query_handler(lambda x: x.data and x.data.startswith('pop '))
async def push_year_inline(callback_query : types.CallbackQuery):
     read= await zodiacDB.sql_year_read(callback_query.data.replace('pop ',''))
     for ink in read:
          await callback_query.message.answer(f'<b><i>{ink[1]}</i></b>\n<b>Описание</b>: {ink[2]}')
     await callback_query.message.answer(f'<i>Понравилось?😊</i>\n\nДля продолжения работы с ботом нажмите меню👇\n\n<b>Забыли команду? Нажмите /help</b>💡', disable_web_page_preview=True)
     await callback_query.answer()
     await bot.edit_message_reply_markup(
        chat_id=callback_query.from_user.id,
        message_id=callback_query.message.message_id, 
        reply_markup=None
    )
     await bot.delete_message(chat_id=callback_query.from_user.id, message_id=callback_query.message.message_id)

# @dp.message_handler(commands=['Китайский гороскоп'])
async def commands_push_year_DB(message : types.Message): 
     await bot.send_message(message.from_user.id,f'<b>Не знаешь как рассчитать свой китайский знак зодиака?</b>🙊\nПереходи быстрей по <b><a href="https://thegirl.ru/articles/pravilnyi-kitaiskii-goroskop-u-tebya-na-samom-dele-chetyre-zhivotnykh-pokrovitelya/">cсылке</a></b> и читай статью об этом', disable_web_page_preview=True)
     await bot.send_message(message.from_user.id, text='Выберите нужный знак зодиака:',reply_markup=ini_year) 
     await message.delete()       

# @dp.message_handler(commands=['Знаки зодиака'])
async def commands_push_DB(message : types.Message): 
     await bot.send_message(message.from_user.id, text='Выберите нужный знак зодиака:',reply_markup=ini_client) 
     await message.delete()    

   
# Ксюшин код
class user_reg (StatesGroup):
    name = State()
    birthday = State()
    feedback = State()

@dp.message_handler(state=user_reg.name)
async def add_name_(message:types.Message, state = FSMContext):
    chat_id = message.from_user.id
    await state.finish()
    zodiacDB.add_user_name(message)
    await bot.send_message(chat_id, "Напишите вашу дату рождения в формате <i>ДД/ММ/ГГГГ</i>")
    await user_reg.birthday.set()

@dp.message_handler(state=user_reg.birthday)
async def add_birthday_(message:types.Message, state=FSMContext):
    chat_id=message.chat.id
    await state.finish()
    zodiacDB.add_user_birthday(message)
    await bot.send_message(chat_id,"Регистрация успешно завершена😊\n\nДля продолжения работы с ботом нажмите меню👇\n\n<b>Забыли команду? Нажмите /help</b>💡")

# @dp.message_handler(commands=['drop'])
async def drop_message(message:types.Message, state=FSMContext):
    chat_id=message.from_user.id
    zodiacDB.drop_user_reg(chat_id)
    await bot.send_message(chat_id,"<b>Запись о вас успешно удалена!</b>\nДля повторной регистрации нажмите <b>/reg</b>\n\nДля продолжения работы с ботом нажмите меню👇\n\n<b>Забыли команду? Нажмите /help</b>💡")

# @dp.message_handler(commands=['update'])
async def drop_review(message:types.Message, state=FSMContext):
    chat_id=message.from_user.id
    zodiacDB.update_user_review(chat_id)
    await bot.send_message(chat_id,"<b>Ваш голос успешно удален!</b>\nДля повторного голосования нажмите <b>/review</b>\n\nДля продолжения работы с ботом нажмите меню👇\n\n<b>Забыли команду? Нажмите /help</b>💡")

# @dp.message_handler(commands=['reg'])
async def start_message(message:types.Message, state=FSMContext):
    chat_id = message.chat.id
    user_status = zodiacDB.add_user(message)
    if user_status == False:
        user_name = zodiacDB.get_user_name(chat_id)
        user_birthday = zodiacDB.get_user_birthday(chat_id)
        await bot.send_message(chat_id,"<i>Введенные данные:</i> \n"
                                        f"Ваше имя: {user_name}\n"
                                        f"Ваша дата рождения: {user_birthday}\n"
                                        f"Для прохождения регистрации повторно, используйте команду <b>/drop</b>")
                                        
    else:
        await bot.send_message(chat_id, f"Привет!✋ {message.chat.first_name} !\n"
                                        f"Введите Ваше имя")
        await user_reg.name.set()

# @dp.message_handler(commands=['prediction'])
async def random_prediction(message:types.Message, state=FSMContext):
        chat_id=message.from_user.id
        average_message=zodiacDB.get_prediction1()+zodiacDB.get_prediction2()+zodiacDB.get_prediction3()
        await bot.send_message(chat_id,"🔮Ваше предсказание на сегодня: \n"
                                        f"{average_message}")
# @dp.message_handler(commands=['nat_karta'])
async def nat_karta_com(message:types.Message):
        await bot.send_message(message.from_user.id,'❗Чтобы посчитать свою натальную карту, перейдите по <b><a href="https://geocult.ru/natalnaya-karta-onlayn-raschet">cсылке</a></b> и введите свои данные: <b>дату рождения</b> и <b>время рождения</b>, а также <b>место рождения</b>\n\nДля продолжения работы с ботом нажмите меню👇\n\n<b>Забыли команду? Нажмите /help</b>💡', disable_web_page_preview=True)
                                  
        
        
# @dp.message_handler(commands =['feedback'])
async def Text_feed(message:types.Message, state = FSMContext):
    chat_id = message.from_user.id
    user_status = zodiacDB.add_feed(message)
    if user_status == False:
        await bot.send_message(chat_id, "Спасибо за Ваш отзыв!😊")
    else  :
        await bot.send_message(chat_id, "Оставьте отзыв о продукте.\nНапишите его сильные и слабые стороны.\nПожалуйста, будьте корректны")
        await user_reg.feedback.set()

# @dp.message_handler(state=user_reg.feedback)
async def add_feedback_(message:types.Message, state = FSMContext):
    chat_id = message.from_user.id
    await state.finish()
    zodiacDB.add_user_feedback(message)
    await bot.send_message(chat_id, "Спасибо за Ваш отзыв!")  

        
# Парсинг сайта 
@dp.callback_query_handler(lambda x: x.data and x.data.startswith('url '))
async def push_year_inline(callback_query : types.CallbackQuery):
     read= await zodiacDB.sql_url_read(callback_query.data.replace('url ',''))
     headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36"
    }
     for line in read:
         url=f'{line[2]}'
     r = requests.get(url=url, headers=headers)
     soup = BeautifulSoup(r.text, "lxml")
     articles_cards = soup.find_all("div", class_="mainContainer")
     for article in articles_cards:
        article_title = article.find("h1").text.strip()
        article_text = article.find("p", class_="").text.strip()
        await callback_query.message.answer(f"<b>{article_title}</b>\n{article_text}")
        await callback_query.message.answer(f'<i>Понравилось?</i>😊\n\nДля продолжения работы с ботом впишите необходимую вам функцию в строку\n\n<b>Для дальнейшей работы с ботом нажмите на меню👇</b>\n\n<b>Забыли команду? Нажмите /help</b>💡', disable_web_page_preview=True)
        await callback_query.answer()
        await bot.edit_message_reply_markup(
        chat_id=callback_query.from_user.id,
        message_id=callback_query.message.message_id, 
        reply_markup=None
    )


@dp.message_handler(commands=['horoscope'])
async def get_first_zodiac(message : types.Message):
    await bot.send_message(message.from_user.id, text='Выберите знак зодиака, у которого вы бы хотели посмотреть гороскоп на сегодня:', reply_markup=ini_client_url)
    

@dp.callback_query_handler(lambda x: x.data and x.data.startswith('year_url '))
async def push_year_inline(callback_query : types.CallbackQuery):
     read= await zodiacDB.sql_year_url_read(callback_query.data.replace('year_url ',''))
     headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36"
    }
     for line in read:
         url=f'{line[2]}'
     r = requests.get(url=url, headers=headers)
     soup = BeautifulSoup(r.text, "lxml")
     articles_cards = soup.find_all("div", class_="mainContainer")
     for article in articles_cards:
        article_title = article.find("h1").text.strip()
        article_text = article.find("p", class_="").text.strip()
        await callback_query.message.answer(f"<b>{article_title}</b>\n{article_text}")
        await callback_query.message.answer(f'<i>Понравилось?</i>😊\n\nДля продолжения работы с ботом впишите необходимую вам функцию в строку\n\n<b>Для дальнейшей работы с ботом нажмите на меню👇</b>\n\n<b>Забыли команду? Нажмите /help</b>💡', disable_web_page_preview=True)
        await callback_query.answer()
        await bot.edit_message_reply_markup(
        chat_id=callback_query.from_user.id,
        message_id=callback_query.message.message_id, 
        reply_markup=None
    )


@dp.message_handler(commands=['year_horoscope'])
async def get_first_zodiac(message : types.Message):
    await bot.send_message(message.from_user.id, text='Выберите знак зодиака, у которого вы бы хотели посмотреть гороскоп на сегодня:', reply_markup=ini_yearclient_url)   
   

        

def register_handlers_client(dp : Dispatcher):
    dp.register_message_handler(message_start, commands=['start'])
    dp.register_message_handler(commands_start,commands=['help'])
    dp.register_message_handler(commands_push_DB, commands=['zodiac'])
    dp.register_message_handler(commands_push_year_DB, commands=['china_zodiac'])
    dp.register_message_handler(random_prediction, commands=['prediction'])
    dp.register_message_handler(start_message, commands=['reg'])
    dp.register_message_handler(drop_review, commands=['update'])
    dp.register_message_handler(drop_message, commands=['drop'])
    dp.register_message_handler(Text_feed, commands =['feedback'])
    dp.register_message_handler(add_feedback_, state=user_reg.feedback)
    dp.register_message_handler(nat_karta_com, commands=['karta'])
