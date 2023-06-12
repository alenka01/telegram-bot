from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.utils.callback_data import CallbackData

cb = CallbackData('mark', 'action')
key1 = InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text='Оставить отзыв',callback_data='mark:reg')]])
key2 = InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text='Дальнейшая работа программы...', callback_data='mark:start')]])

ini_client=InlineKeyboardMarkup(row_width=1)

iniButton_1=InlineKeyboardButton(text='Овен',callback_data=f'del {1}')
iniButton_2=InlineKeyboardButton(text='Телец',callback_data=f'del {2}')
iniButton_3=InlineKeyboardButton(text='Близнецы',callback_data=f'del {3}')
iniButton_4=InlineKeyboardButton(text='Рак',callback_data=f'del {4}')
iniButton_5=InlineKeyboardButton(text='Лев',callback_data=f'del {5}')
iniButton_6=InlineKeyboardButton(text='Дева',callback_data=f'del {6}')
iniButton_7=InlineKeyboardButton(text='Весы',callback_data=f'del {7}')
iniButton_8=InlineKeyboardButton(text='Скорпион',callback_data=f'del {8}')
iniButton_9=InlineKeyboardButton(text='Стрелец',callback_data=f'del {9}')
iniButton_10=InlineKeyboardButton(text='Козерог',callback_data=f'del {10}')
iniButton_11=InlineKeyboardButton(text='Водолей',callback_data=f'del {11}')
iniButton_12=InlineKeyboardButton(text='Рыбы',callback_data=f'del {12}')

ini_client.row(iniButton_1,iniButton_2).row(iniButton_3,iniButton_4).row(iniButton_5,iniButton_6).row(iniButton_7,iniButton_8).row(iniButton_9,iniButton_10).row(iniButton_11,iniButton_12)

ini_year=InlineKeyboardMarkup(row_width=1)

yearButton_1=InlineKeyboardButton(text='Крыса',callback_data=f'pop {1}')
yearButton_2=InlineKeyboardButton(text='Бык/Вол',callback_data=f'pop {2}')
yearButton_3=InlineKeyboardButton(text='Тигр',callback_data=f'pop {3}')
yearButton_4=InlineKeyboardButton(text='Кот/Кролик',callback_data=f'pop {4}')
yearButton_5=InlineKeyboardButton(text='Дракон',callback_data=f'pop {5}')
yearButton_6=InlineKeyboardButton(text='Змея',callback_data=f'pop {6}')
yearButton_7=InlineKeyboardButton(text='Конь/Лошадь',callback_data=f'pop {7}')
yearButton_8=InlineKeyboardButton(text='Овца/Коза',callback_data=f'pop {8}')
yearButton_9=InlineKeyboardButton(text='Обезьяна',callback_data=f'pop {9}')
yearButton_10=InlineKeyboardButton(text='Петух',callback_data=f'pop {10}')
yearButton_11=InlineKeyboardButton(text='Пес/Собака',callback_data=f'pop {11}')
yearButton_12=InlineKeyboardButton(text='Кабан/Свинья',callback_data=f'pop {12}')

ini_year.row(yearButton_1,yearButton_2).row(yearButton_3,yearButton_4).row(yearButton_5,yearButton_6).row(yearButton_7,yearButton_8).row(yearButton_9,yearButton_10).row(yearButton_11,yearButton_12)

ini_client_url=InlineKeyboardMarkup(row_width=1)

ini_url_Button_1=InlineKeyboardButton(text='Овен',callback_data=f'url {1}')
ini_url_Button_2=InlineKeyboardButton(text='Телец',callback_data=f'url {2}')
ini_url_Button_3=InlineKeyboardButton(text='Близнецы',callback_data=f'url {3}')
ini_url_Button_4=InlineKeyboardButton(text='Рак',callback_data=f'url {4}')
ini_url_Button_5=InlineKeyboardButton(text='Лев',callback_data=f'url {5}')
ini_url_Button_6=InlineKeyboardButton(text='Дева',callback_data=f'url {6}')
ini_url_Button_7=InlineKeyboardButton(text='Весы',callback_data=f'url {7}')
ini_url_Button_8=InlineKeyboardButton(text='Скорпион',callback_data=f'url {8}')
ini_url_Button_9=InlineKeyboardButton(text='Стрелец',callback_data=f'url {9}')
ini_url_Button_10=InlineKeyboardButton(text='Козерог',callback_data=f'url {10}')
ini_url_Button_11=InlineKeyboardButton(text='Водолей',callback_data=f'url {11}')
ini_url_Button_12=InlineKeyboardButton(text='Рыбы',callback_data=f'url {12}')

ini_client_url.row(ini_url_Button_1,ini_url_Button_2).row(ini_url_Button_3,ini_url_Button_4).row(ini_url_Button_5,ini_url_Button_6).row(ini_url_Button_7,ini_url_Button_8).row(ini_url_Button_9,ini_url_Button_10).row(ini_url_Button_11,ini_url_Button_12)

ini_yearclient_url=InlineKeyboardMarkup(row_width=1)

ini_url_yearButton_1=InlineKeyboardButton(text='Крыса',callback_data=f'year_url {1}')
ini_url_yearButton_2=InlineKeyboardButton(text='Бык/Вол',callback_data=f'year_url {2}')
ini_url_yearButton_3=InlineKeyboardButton(text='Тигр',callback_data=f'year_url {3}')
ini_url_yearButton_4=InlineKeyboardButton(text='Кот/Кролик',callback_data=f'year_url {4}')
ini_url_yearButton_5=InlineKeyboardButton(text='Дракон',callback_data=f'year_url {5}')
ini_url_yearButton_6=InlineKeyboardButton(text='Змея',callback_data=f'year_url {6}')
ini_url_yearButton_7=InlineKeyboardButton(text='Конь/Лошадь',callback_data=f'year_url {7}')
ini_url_yearButton_8=InlineKeyboardButton(text='Овца/Коза',callback_data=f'year_url {8}')
ini_url_yearButton_9=InlineKeyboardButton(text='Обезьяна',callback_data=f'year_url {9}')
ini_url_yearButton_10=InlineKeyboardButton(text='Петух',callback_data=f'year_url {10}')
ini_url_yearButton_11=InlineKeyboardButton(text='Пес/Собака',callback_data=f'year_url {11}')
ini_url_yearButton_12=InlineKeyboardButton(text='Кабан/Свинья',callback_data=f'year_url {12}')

ini_yearclient_url.row(ini_url_yearButton_1,ini_url_yearButton_2).row(ini_url_yearButton_3,ini_url_yearButton_4).row(ini_url_yearButton_5,ini_url_yearButton_6).row(ini_url_yearButton_7,ini_url_yearButton_8).row(ini_url_yearButton_9,ini_url_yearButton_10).row(ini_url_yearButton_11,ini_url_yearButton_12)