import telebot 
from telebot import types
from dotenv import load_dotenv
import os

load_dotenv()
bot_TOKEN = os.getenv('TOKEN')
bot = telebot.Telebot(bot_TOKEN)


