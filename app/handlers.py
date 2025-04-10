import os,telebot
from telebot import types
from dotenv import load_dotenv
load_dotenv()

#TOKEN = os.getenv("TOKEN")
TOKEN = "7614655036:AAE_8ucrC55szdKOlbTnfbU4tB5UpoB1_Vo"
CATEGORY = os.getenv("CATEGORY").split(",")
def unpack(d):
    a = dict()
    d = d.split("},")
    g = list()
    for i in range(len(d)):
        g.append(d[i].replace("}","")[d[i].find("{")+1:].split(","))
        a[d[i][:d[i].find(":")]]=g[i]
    #while s.find(":"):
    #    a[s[0:s.find("{")-1]]= s[s.find("{")+1:s.find("}")].split(",")
    #    s = (s[s.find("},")+2:])
    return a
GUNS = unpack(os.getenv("GUNS"))
tmp = list(GUNS.keys())[0]

bot = telebot.TeleBot(TOKEN,parse_mode=None)
@bot.message_handler(commands=['start'])
def welcome(message):
    markup = types.InlineKeyboardMarkup()
    for tip in CATEGORY:
        markup.add(types.InlineKeyboardButton(tip,callback_data=tip))
    bot.reply_to(message, "Выберите тип оружия:",reply_markup=markup)
    #bot.register_next_step_handler(message,on_click)
def menu(message):
    markup = types.InlineKeyboardMarkup()
    for gun in GUNS[tmp]:
        markup.add(types.InlineKeyboardButton(gun,callback_data=gun))
    bot.reply_to(message, "Выберите тип оружия:",reply_markup=markup)

#def on_click(message):
#   if True:
#        bot.send_message(message.chat.id,message.text)
#        markup = types.ReplyKeyboardMarkup()
#        for gun in GUNS:
#            markup.add(types.KeyboardButton(tip))#,callback_data=tip))
#        bot.reply_to(message, "Выберите тип оружия:",reply_markup=markup)
#        bot.register_next_step_handler(message,on_click2)

@bot.callback_query_handler(func=lambda callback: True)
def callback_message(callback):
    for tip in CATEGORY:
        if callback.data == tip:
            tmp=tip
            bot.send_message(callback.message.chat.id,tip)
            menu(callback.message)
    for gun in GUNS[tmp]:
        if callback.data == gun:
            bot.send_message(callback.message.chat.id,gun)
bot.infinity_polling()