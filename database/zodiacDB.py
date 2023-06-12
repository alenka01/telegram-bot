import sqlite3 as sq
from create_bot import dp, bot
from aiogram.dispatcher.filters import Command
from keyboards import key1, key2, cb
from aiogram.types import Message,CallbackQuery,PollAnswer
import random

def sql_start():
    global db,cur
    db= sq.connect('zodiac_db1.db')
    db.execute("PRAGMA journal_mode=WAL")
    cur=db.cursor()
    if db:
        print('Database connected OK!')
    db.execute('CREATE TABLE IF NOT EXISTS astrologZodiac(astrolZodiacID INT PRIMARY KEY, astrolZodiacName TEXT, astrolZodiacFirstDate TEXT, astrolZodiacLastDate TEXT, astrolZodiacSpec TEXT)')
    db.execute('CREATE TABLE IF NOT EXISTS yearZodiac(yearZodiacID INT PRIMARY KEY, yearZodiacName TEXT, yearZodiacSpec TEXT)')
    db.execute('CREATE TABLE IF NOT EXISTS users(id INT PRIMARY KEY, name TEXT, birthday TEXT)')
    db.execute('CREATE TABLE IF NOT EXISTS user_review(user_id INT PRIMARY KEY, name TEXT, review TEXT)')
    db.execute('CREATE TABLE IF NOT EXISTS generation(id INT PRIMARY KEY, first_part TEXT, middle_part TEXT, last_part TEXT)')
    db.execute('CREATE TABLE IF NOT EXISTS zodiac_url(zodiac_id INT PRYMARY KEY, zodiac_name TEXT, url TEXT)')
    db.execute('CREATE TABLE IF NOT EXISTS year_zodiac_url(year_zodiac_id INT PRYMARY KEY, year_zodiac_name TEXT, year_url TEXT)')
    db.execute('CREATE TABLE IF NOT EXISTS feedback(user_id INT PRYMARY KEY, text TEXT)')
    db.commit()

async def sql_read(data):
    read = cur.execute('SELECT * FROM astrologZodiac WHERE astrolZodiacID = ?', (data,)).fetchall()
    return(read)

async def sql_year_read(data):
    read_y = cur.execute('SELECT * FROM yearZodiac WHERE yearZodiacID = ?', (data,)).fetchall()
    return(read_y)

async def sql_url_read(data):
    read = cur.execute('SELECT * FROM zodiac_url WHERE zodiac_id = ?', (data,)).fetchall()
    return(read)

async def sql_year_url_read(data):
    read = cur.execute('SELECT * FROM year_zodiac_url WHERE year_zodiac_id = ?', (data,)).fetchall()
    return(read)



# Ксюшин код 

def add_feed(message):
    cur.execute("SELECT user_id FROM feedback WHERE user_id=?", (message.from_user.id,))
    user = cur.fetchone()
    if not user:
        cur.execute("INSERT INTO feedback VALUES (?, ?)",(message.from_user.id, "text",))
        db.commit()
    else:
        return False
def add_user_feedback(message):
    cur.execute("UPDATE feedback SET text=? WHERE user_id=?", (message.text,message.from_user.id,))
    db.commit()
    db.close()

def add_user(message):
    cur.execute("SELECT id FROM users WHERE id=?", (message.chat.id,))
    user = cur.fetchone()
    if not user:
        cur.execute("INSERT INTO users VALUES (?,?,?)",(message.chat.id, "name",'birthday'))
        db.commit()
    else:
        return False
def add_user_name(message):
    cur.execute("UPDATE users SET name=? WHERE id=?", (message.text,message.chat.id,))
    db.commit()
def drop_user_reg(user_id):
    cur.execute("DELETE FROM users WHERE id=?",(user_id,))
    db.commit()
def update_user_review(user_id):
    cur.execute("DELETE FROM user_review WHERE user_id=?",(user_id,))
    cur.execute("DELETE FROM feedback WHERE user_id=?",(user_id,))
    db.commit()
def add_user_birthday(message):
    cur.execute("UPDATE users SET birthday=? WHERE id=?", (message.text,message.chat.id,))
    db.commit()
def get_user_name (user_id):
    cur.execute("SELECT name FROM users WHERE id=?",(user_id,))
    user_name = cur.fetchone()[0]
    return user_name
def get_user_birthday (user_id):
    cur.execute("SELECT birthday FROM users WHERE id=?",(user_id,))
    user_birthday = cur.fetchone()[0]
    return user_birthday

prediction_id = random.randint(0, 3)
def get_prediction1 ():
    cur.execute("SELECT first_part FROM generation ORDER BY RANDOM() LIMIT 1")
    first_prediction = cur.fetchone()[0]
    return first_prediction
prediction_id2 = random.randint(0, 3)
def get_prediction2 ():
    cur.execute("SELECT middle_part FROM generation ORDER BY RANDOM() LIMIT 1")
    middle_prediction = cur.fetchone()[0]
    return middle_prediction
prediction_id3 = random.randint(0, 3)
def get_prediction3 ():
    cur.execute("SELECT last_part FROM generation ORDER BY RANDOM() LIMIT 1")
    last_prediction = cur.fetchone()[0]
    return last_prediction


@dp.message_handler(Command('review'))
async def start (message: Message):
    connect = sq.connect('zodiac_db1.db')
    cursor = connect.cursor()
    cursor.execute("""INSERT INTO user_review (user_id, name) VALUES(?, ?)""",[message.chat.id, message.chat.first_name])
    connect.commit()
    cursor.close()
    connect.close()
    await bot.send_message(chat_id=message.chat.id, text='Понравилось со мной взаимодействовать?😊\nТогда оставь отзыв ниже👇', reply_markup=key1)
@dp.callback_query_handler(cb.filter(action='reg'))
async def registration (call: CallbackQuery):
    await call.answer(cache_time=10)
    await bot.send_poll(chat_id=call.message.chat.id,
                        question='Что думаешь?',
                        options=['Мне всё нравится, добавлять ничего не надо!','Мне всё нравится, но можно что-то добавить, напишу об этом ниже','Мне не понравилось, напишу ниже почему'], is_anonymous=False, allows_multiple_answers=False)
    await bot.send_message(chat_id=call.message.chat.id, text='<b>Спасибо за предоставленную информацию!</b>\nЕсли вы хотите оставить письменный отзыв, пожалуйста, нажмите на /feedback\n\nЧтобы удалить свой голос нажмите /update\n\nДля дальнейшей работы с ботом введите в строку необходимую команду\n\nДля открытия сообщения со всеми функциями нажмите /help')
@dp.poll_answer_handler()
async def hanle_poll_answer(poll: PollAnswer):
    connect = sq.connect('zodiac_db1.db')
    cursor = connect.cursor()
    review = str(poll['option_ids'])
    user_id = poll['user']['id']
    cursor.execute("""UPDATE user_review SET review=(?) WHERE user_id=(?)""", [review, user_id])
    cursor.close()
    connect.commit()
    connect.close()

    


   