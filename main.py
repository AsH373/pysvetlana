
#import pyTelegramBotAPI
import telebot

bot =  telebot.TeleBot('5688000369:AAFMhLZ4Nbvf3BTM0GcQSf5x8mOahKhZwL8')
@bot.message_handler(comamnds = ['start'])
@bot.message_handler(content_types = ['text'])
def repeat(message):
    bot.send_message(message.chat.id, message.text)
bot.polling(non_stop = True)
