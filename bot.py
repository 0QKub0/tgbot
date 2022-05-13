import telebot
from telebot import types
import random
x = 1
y = 2
number = [x,y]
random_1 = random.choice(number)

bot = telebot.TeleBot("API_TOKEN")

@bot.message_handler(commands=['start'])
def start(message):
    mess1 = f'<b>Привіт, {message.from_user.first_name} \nЦе мій перший телеграм бот ;) </b>'
    bot.send_message(message.chat.id, mess1 , parse_mode='html')
    sti = open('../sticker.webp', 'rb')
    bot.send_sticker(message.chat.id, sti)
    bot.send_sticker(message.chat.id, "FILEID")

@bot.message_handler(commands=['help'])
def help(message):
    mess2 = f'Допомоги не буде :)'
    bot.send_message(message.chat.id, mess2, parse_mode='html')
    sti = open('../sticker2.webp', 'rb')
    bot.send_sticker(message.chat.id, sti)
    bot.send_sticker(message.chat.id, "FILEID")

@bot.message_handler(commands=['website'])
def website(message):
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton("Наш вебсайт", url="http://surl.li/ygyr"))
    bot.send_message(message.chat.id, 'Посилання на сайт', reply_markup=markup)

@bot.message_handler()
def get_user_text(message):
    bot.send_message(message.chat.id, message, parse_mode='html')

@bot.message_handler(content_types=['photo'])
def get_user_photo(message):
    bot.send_message(message.chat.id, 'вау')
    sti = open('../sticker3.webp', 'rb')
    bot.send_sticker(message.chat.id, sti)
    bot.send_sticker(message.chat.id, "FILEID")

@bot.message_handler(content_types=['video'])
def get_user_video(message):
    bot.send_message(message.chat.id, 'ІЗІ')
    sti = open('../sticker4.webp', 'rb')
    bot.send_sticker(message.chat.id, sti)
    bot.send_sticker(message.chat.id, "FILEID")

@bot.message_handler(content_types=['sticker'])
def get_user_sticker(message):
    if random_1 == 1:
        sti = open('../sticker5.webp', 'rb')
        bot.send_sticker(message.chat.id, sti)
        bot.send_sticker(message.chat.id, "FILEID")
    elif random_1 == 2:
        sti = open('../sticker6.webp', 'rb')
        bot.send_sticker(message.chat.id, sti)
        bot.send_sticker(message.chat.id, "FILEID")



bot.polling(none_stop=True)