from telebot import types
from app.main import bot  # импорт объекта

@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, 'Привет!')

@bot.message_handler(commands=['button'])
def button_message(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton("Помощь")
    markup.add(item1)
    bot.send_message(message.chat.id, "Выберите опцию:", reply_markup=markup)
