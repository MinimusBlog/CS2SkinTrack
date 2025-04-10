from main import bot
from telebot import types

@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, 'Привет!')

@bot.message_handler(commands=['button'])
def button_message(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton("Помощь")
    markup.add(item1)
    bot.send_message(message.chat.id, "Выберите ...", reply_markup=markup)
