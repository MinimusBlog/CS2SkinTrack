import telebot 
from telebot import types
import os

@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id,'Привет и добро пожаловать в CS2 SkinTrack бот, здесь ты сможешь посмотреть, как выглядит скин и его стоимость с НДС и без.')