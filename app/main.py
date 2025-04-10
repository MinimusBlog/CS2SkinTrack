# app/main.py

import telebot
from dotenv import load_dotenv
import os

load_dotenv()
bot_TOKEN = os.getenv('TOKEN')
bot = telebot.TeleBot(bot_TOKEN)

import handlers # импорт обработчиков

if __name__ == "__main__":
    bot.polling(none_stop=True)
