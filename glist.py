import telebot
bot = telebot.TeleBot('5688000369:AAFMhLZ4Nbvf3BTM0GcQSf5x8mOahKhZwL8')


@bot.message_handler(commands=['start'])
def start(message):
    claviatura = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
    cnopka1 = telebot.types.KeyboardButton('Yes')
    cnopka2 = telebot.types.KeyboardButton('No')
    claviatura.add(cnopka1, cnopka2)
    bot.send_message(message.chat.id, text='Привет давай сыграем в игру)', reply_markup=claviatura)




@bot.message_handler(content_types=['text'])
def init(message):
    if message.text=="No":
        bot.send_photo(message.chat.id,"https://www.meme-arsenal.com/memes/2c674e1831c37a01c7ff8ab6f24bb7b8.jpg")
        claviatura = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
        cnopka1 = telebot.types.KeyboardButton('Начать заныва')
        cnopka2 = telebot.types.KeyboardButton("https://t.me/svetik_and_code")
        claviatura.add(cnopka1, cnopka2)
        bot.send_message(message.chat.id, text="Перейдите Светлана будет давольна ", reply_markup=claviatura)
    if message.text=="Yes":
        claviatura = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
        cnopka1 = telebot.types.KeyboardButton('Лазарева')
        cnopka2 = telebot.types.KeyboardButton('Бузова')
        cnopka3 = telebot.types.KeyboardButton('Пугачёва')
        cnopka4 = telebot.types.KeyboardButton('Шакурова')
        cnopka5 = telebot.types.KeyboardButton('Ростелеконова')
        cnopka6 = telebot.types.KeyboardButton('Нагиева')
        claviatura.add(cnopka1, cnopka2, cnopka3, cnopka4, cnopka5, cnopka6)
        bot.send_message(message.chat.id, text="Какая фамилия у Светланы", reply_markup=claviatura)
    if message.text=="Шакурова":
        bot.send_message(message.chat.id, text="Молодец возьми с полки пиражочек")
        claviatura = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
        cnopka1 = telebot.types.KeyboardButton("Вероника")
        cnopka2 = telebot.types.KeyboardButton('Космонавт')
        cnopka3 = telebot.types.KeyboardButton('Президент Перми')
        cnopka4 = telebot.types.KeyboardButton('Многодетная мать')
        cnopka5 = telebot.types.KeyboardButton('Программист')
        cnopka6 = telebot.types.KeyboardButton('Биссектриса')
        claviatura.add(cnopka1, cnopka2, cnopka3, cnopka4, cnopka5, cnopka6)
        bot.send_message(message.chat.id, text="Кто такая Светлана?", reply_markup=claviatura)
    if message.text=="Программист":
        bot.send_message(message.chat.id, text="Молодец возьми на кухне борщ")
        claviatura = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
        cnopka1 = telebot.types.KeyboardButton("Органы")
        cnopka2 = telebot.types.KeyboardButton('Малекулы')
        cnopka3 = telebot.types.KeyboardButton('Воды')
        cnopka4 = telebot.types.KeyboardButton('Неорганические вещества')
        claviatura.add(cnopka1, cnopka2, cnopka3, cnopka4)
        bot.send_message(message.chat.id, text="Из чего состоит больше всего Светлана??", reply_markup=claviatura)
    if message.text=="Воды":
        bot.send_message(message.chat.id, text="Ъ")
        claviatura = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
        cnopka1 = telebot.types.KeyboardButton("Кто?")
        cnopka2 = telebot.types.KeyboardButton('Что?')
        cnopka3 = telebot.types.KeyboardButton('Когда?')
        cnopka4 = telebot.types.KeyboardButton('Зачем?')
        cnopka5 = telebot.types.KeyboardButton('Почему?')
        cnopka6 = telebot.types.KeyboardButton('Как?')
        claviatura.add(cnopka1, cnopka2, cnopka3, cnopka4, cnopka5, cnopka6)
        bot.send_message(message.chat.id, text=" Светлана?", reply_markup=claviatura)
    if message.text=="Кто?":
        bot.send_message(message.chat.id, text="Лаки")
        claviatura = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
        cnopka1 = telebot.types.KeyboardButton("Вероника")
        cnopka2 = telebot.types.KeyboardButton('Космонавт')
        cnopka3 = telebot.types.KeyboardButton('Президент Перми')
        cnopka4 = telebot.types.KeyboardButton('Многодетная мать')
        cnopka5 = telebot.types.KeyboardButton('Программист')
        cnopka6 = telebot.types.KeyboardButton('Потеряшка')
        claviatura.add(cnopka1, cnopka2, cnopka3, cnopka4, cnopka5, cnopka6)
        bot.send_message(message.chat.id, text="Кто такая Светлана?", reply_markup=claviatura)
bot.polling(non_stop=True)
