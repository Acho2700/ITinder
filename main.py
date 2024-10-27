import telebot
from telebot import types

bot = telebot.TeleBot('7855213389:AAFdmLy9DS1HJ39MuPaO48XKogYtvuKihOw')

@bot.message_handler(commands=['start'])
def command_start(message):
    markup =  types.ReplyKeyboardMarkup()
    btn_1 = types.KeyboardButton('Вступить в команду')
    btn_2 = types.KeyboardButton('Найти команду')
    markup.add(btn_1, btn_2)
    bot.send_message(message.chat.id, 'Привет, я бот для поиска IT команды \n Выбери что хочешь сделать:', reply_markup=markup)




@bot.message_handler()
def text_handler(message):
    if message.text == 'Вступить в команду':
        bot.send_message(message.chat.id, 'Пожалуйста, введите данные о себе ( через запятую ) \n ФИО, Факультет', reply_markup=types.ReplyKeyboardRemove())
        bot.register_next_step_handler(message, worker_reg_fio)
    elif message.text == 'Меню' or message.text == 'Назад в Меню':
        markup = types.ReplyKeyboardMarkup()
        btn_1 = types.KeyboardButton('Изменить Анкету')
        btn_2 = types.KeyboardButton('Выключить анкету')
        btn_3 = types.KeyboardButton('Моя Анкета')
        btn_4 = types.KeyboardButton('Искать проект')
        markup.add(btn_1, btn_2, btn_3, btn_4)
        bot.send_message(message.chat.id, 'Вы в меню', reply_markup=markup)
    elif message.text == 'Изменить Анкету':
        edit_anket(message)
    elif message.text == 'ФИО':
        bot.send_message(message.chat.id, 'Введите новое ФИО')
        bot.register_next_step_handler(message, edit_fio)
    elif message.text == 'Направление':
        bot.send_message(message.chat.id, 'Введите новое Направление')
        bot.register_next_step_handler(message, edit_direction)
    elif message.text == 'Навыки':
        pass
    elif message.text == 'Добавить':
        pass
    elif message.text == 'Удалить':
        pass
    elif message.text == 'Проекты':
        pass
    elif message.text == 'Моя Анкета':
        worker_anket(message)



dict_worker = dict()
def worker_reg_fio(message):
    global dict_worker
    text = message.text.split(',')
    id_worker = message.from_user.id
    dict_worker[id_worker] = text
    bot.send_message(message.chat.id, f'Вы {text[0]}, ваше направление {text[1]}')
    bot.send_message(message.chat.id, 'Теперь расскажите о своих навыках')
    bot.register_next_step_handler(message, worker_reg_text)

def worker_reg_text(message):
    markup = types.ReplyKeyboardMarkup()
    btn_1 = types.KeyboardButton('Меню')
    markup.add(btn_1)

    global dict_worker
    text = message.text
    id_worker = message.from_user.id
    dict_worker[id_worker].append(text)
    bot.send_message(message.chat.id, 'Вот ваша анкета:')
    bot.send_message(message.chat.id, f'{dict_worker[id_worker][0]} \n Факультет: {dict_worker[id_worker][1]} \n О себе: {dict_worker[id_worker][2]}', reply_markup=markup)

def worker_anket(message):
    markup = types.ReplyKeyboardMarkup()
    btn_1 = types.KeyboardButton('Меню')
    markup.add(btn_1)
    id_worker = message.from_user.id
    bot.send_message(message.chat.id, f'{dict_worker[id_worker][0]} \n Факультет: {dict_worker[id_worker][1]} \n О себе: {dict_worker[id_worker][2]}', reply_markup=markup)

def edit_anket(message):
    markup = types.ReplyKeyboardMarkup()
    btn_1 = types.KeyboardButton('ФИО')
    btn_2 = types.KeyboardButton('Направление')
    btn_3 = types.KeyboardButton('Навыки')
    btn_4 = types.KeyboardButton('Проекты')
    btn_5 = types.KeyboardButton('Назад в Меню')
    markup.add(btn_1, btn_2, btn_3, btn_4, btn_5)
    bot.send_message(message.chat.id, 'Что вы хотите изменить?', reply_markup=markup)

def edit_fio(message):
    markup = types.ReplyKeyboardMarkup()
    btn_1 = types.KeyboardButton('Меню')
    markup.add(btn_1)
    global dict_worker
    id_worker = message.from_user.id
    dict_worker[id_worker][0] = message.text
    bot.send_message(message.chat.id, f'Ваше новое ФИО:  {dict_worker[id_worker][0]}', reply_markup=markup)

def edit_direction(message):
    markup = types.ReplyKeyboardMarkup()
    btn_1 = types.KeyboardButton('Меню')
    markup.add(btn_1)
    global dict_worker
    id_worker = message.from_user.id
    dict_worker[id_worker][1] = message.text
    bot.send_message(message.chat.id, f'Ваше новое Направление:  {dict_worker[id_worker][1]}', reply_markup=markup)

# def add_del(message):
#     markup = types.ReplyKeyboardMarkup()
#     btn_1 = types.KeyboardButton('Добавить')
#     btn_2 = types.KeyboardButton('Удалить')
#     markup.add(btn_1, btn_2)
#     bot.send_message(message.chat.id, 'Выберите действие', reply_markup=markup)


bot.infinity_polling(timeout=10, long_polling_timeout= 5)