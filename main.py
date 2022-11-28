import telebot
from os import remove
bot = telebot.TeleBot('5688000369:AAFMhLZ4Nbvf3BTM0GcQSf5x8mOahKhZwL8')


@bot.message_handler(commands=['start'])
def repea(message):
    bot.send_message(message.chat.id, 'Привет Андрей Плохой Человек')


@bot.message_handler(commands=['help'])
def repeat(message):
    bot.send_message(message.chat.id, 'Это бот повторюшка он за вами будет повторять за тобой')
# @bot.message_handler(comamnds = ['start'])


@bot.message_handler(content_types=['text'])
def repeat(message):
    bot.send_message(message.chat.id, message.text)


@bot.message_handler(content_types=['photo'])
def repet(message):
    svetlana_love = message.photo[-1].file_id
    def_ = bot.get_file(svetlana_love)
    klass = bot.download_file(def_.file_path)
    with open('image', 'wb') as newfile:
        newfile.write(klass)
    apex = open('image', 'rb')
    bot.send_message(message.chat.id, apex)
    apex.close()
    remove('image')


bot.polling(non_stop=True)
