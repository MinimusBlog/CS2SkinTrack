import os,telebot,json
from telebot import types
from dotenv import load_dotenv
load_dotenv()
url = "https://steamcommunity.com/market/listings/730/" #Desert%20Eagle%20%7C%20Sputnik%20%28Battle-Scarred%29"?filter=confetty
get_text = False
#bot = telebot.TeleBot(TOKEN,parse_mode=None)


#from telebot import types
#import logging

# Настройка логирования
#logging.basicConfig(level=logging.INFO)
#logger = logging.getLogger()
def register_handlers(bot):
    get_text = False
    url = "https://steamcommunity.com/market/listings/730/" #Desert%20Eagle%20%7C%20Sputnik%20%28Battle-Scarred%29"
    data_file_path = os.path.join(os.path.dirname(__file__), "data.json")
    with open(data_file_path, "r", encoding="utf-8") as file:
        data = file.read()
    CATEGORY = json.loads(data)["CATEGORY"]#os.getenv("CATEGORY").split(",")
    GUNS = json.loads(data)["GUNS"]
    QUALITY = json.loads(data)["QUALITY"]
    SKINS = json.loads(data)["SKINS"]
    
    @bot.message_handler(commands=['start'])
    def start_message(message):
        #logger.info(f"Отправка /start {message.chat.id}")
        # Создание клавиатуры
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
        item1 = types.KeyboardButton("Помощь")  # Кнопка "Помощь"
        item2 = types.KeyboardButton("Конвертация в USDT")  # Кнопка "Настройки"
        item3 = types.KeyboardButton("Парсинг!") # кнопка запуска
        markup.add(item1, item2,item3)  # Добавляем кнопки в клавиатуру
        bot.send_message(message.chat.id, 'Привет! Выберите действие:', reply_markup=markup)
        

    @bot.message_handler(func=lambda message: message.text == 'Помощь')
    def help_message(message):
        #logger.info(f"Отправка помощи {message.chat.id}")
        instructions = """
        Инструкция по использованию бота:
        1. Выберите действие из меню.
        2. Следуйте инструкциям на экране.
        """
        bot.send_message(message.chat.id, instructions)
    
   

    @bot.callback_query_handler(func=lambda callback: True)
    def callback_message(callback):
        global url
        global get_text
        @bot.message_handler(content_types=['text'])
        def message_input(message):
            global url
            global get_text
            if get_text:
                if len(message.text)>1:
                    url += "?filter="+message.text.replace(" ","%20")
                print(url)
                bot.send_message(message.chat.id,url)
                get_text = False
                
        #bot.register_next_step_handler(callback.message,message_input)
        #bot.delete_message(callback.message.chat.id,callback.message.message_id-1)
        for q in QUALITY:
            if callback.data == q:
                url+= "%28" + callback.data.replace(" ","%20") + "%29"
                get_text = True
                bot.send_message(callback.message.chat.id,"Введите имена стикеров:")
                #bot.send_message(callback.message.chat.id, "Введите имена стикеров:")
                
        for skin in SKINS:
            if callback.data == skin:
                url+= "%7C%20" + callback.data.replace(" ","%20") + "%20"
                menu_quality(callback.message,callback.data)
        for tip in CATEGORY:
            if callback.data == tip:
                #bot.send_message(callback.message.chat.id,callback.data)
                menu_guns(callback.message,callback.data)
                #bot.delete_message(callback.message.chat.id,callback.message.message_id-1)
            for gun in GUNS[tip]:
                if callback.data == gun:
                    url = url + callback.data.replace(" ","%20") + "%20"
                    menu_skins(callback.message,callback.data)
             
        
        
        print(url)
    
    @bot.message_handler(func=lambda message: message.text == 'Парсинг!')
    def menu_category(message):
        markup = types.InlineKeyboardMarkup()
        for tip in CATEGORY:
            markup.add(types.InlineKeyboardButton(tip,callback_data=tip))
        bot.reply_to(message, "Выберите тип оружия:",reply_markup=markup)
#        bot.register_next_step_handler(message,menu_guns)

    def menu_guns(message,tmp):
        markup = types.InlineKeyboardMarkup()
        for gun in GUNS[tmp]:
            markup.add(types.InlineKeyboardButton(gun,callback_data=gun))
        bot.reply_to(message, "Выберите оружие:",reply_markup=markup)
    
    def menu_skins(message,tmp):
        markup = types.InlineKeyboardMarkup()
        for skin in SKINS:
            markup.add(types.InlineKeyboardButton(skin,callback_data=skin))
        bot.reply_to(message, "Выберите скин:",reply_markup=markup)
        

    def menu_quality(message,tmp):
        markup = types.InlineKeyboardMarkup()
        for q in QUALITY:
            markup.add(types.InlineKeyboardButton(q,callback_data=q))
        bot.reply_to(message, "Выберите качество:",reply_markup=markup)


    #def menu_category(message):
    #   bot.send_message(message.chat.id,message.text)
    #   markup = types.ReplyKeyboardMarkup()
    #   for gun in GUNS:
    #       markup.add(types.KeyboardButton(tip))#,callback_data=tip))
    #   bot.reply_to(message, "Выберите оружиt:",reply_markup=markup)
    #   bot.register_next_step_handler(message,on_click2)
