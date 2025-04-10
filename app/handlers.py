import os,telebot,json,requests
from telebot import types
from time import sleep
from dotenv import load_dotenv
from bs4 import BeautifulSoup
load_dotenv()
url = "https://steamcommunity.com/market/listings/730/"
get_text = False
out = False
page = 0
sticker_name = ""
pg = 0
#from telebot import types
#import logging

# Настройка логирования
#logging.basicConfig(level=logging.INFO)
#logger = logging.getLogger()
def register_handlers(bot):
    
    url = "https://steamcommunity.com/market/listings/730/"
    data_file_path = os.path.join(os.path.dirname(__file__), "data.json")
    with open(data_file_path, "r", encoding="utf-8") as file:
        data = file.read()
    CATEGORY = json.loads(data)["CATEGORY"]
    GUNS = json.loads(data)["GUNS"]
    QUALITY = json.loads(data)["QUALITY"]
    
    ALL_SKINS = []
    for tip in CATEGORY:
        for gun in GUNS[tip]:
            ALL_SKINS.append(GUNS[tip][gun])
    
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
        global out
        global page
        global pg
   
        @bot.message_handler(content_types=['text'])
        def message_input(message):
            global page
            global pg
            global url
            global out
            global get_text
            global sticker_name
            if get_text:
                NUM = "0123456789"
                if len(message.text)>1:
                    sticker_name = message.text.replace(" ","+")
                url_render = url+"/render/?filter="+sticker_name+"&query=&start=0&count=10&country=RU&language=russian&currency=1"
                render_req = requests.get(url_render)
                cnt = 54
                while render_req.text[cnt] in NUM:
                    cnt += 1
                bot.send_message(message.chat.id,"всего пушек: "+render_req.text[54:cnt])
                page = int(render_req.text[54:cnt])//10+1
                menu_next(message)
                get_text = False

        if (callback.data=="Далее"):
            PRICE_TYPE = ("market_listing_price_with_fee", "market_listing_price_with_publisher_fee_only", "market_listing_price_without_fee")
            PRICE_TYPE_NAME = ("с комиссией", "с комиссией к публикации", "без комиссии")
            
            bot.send_message(callback.message.chat.id,"="*10+"\n"+str(pg+1)+"-ая страница")
            urll = url+"/?filter="+sticker_name+"&query=&start="+str(pg*10)+"&count=10&country=RU&language=russian&currency=1"
            if pg == 0:
                bot.send_message(callback.message.chat.id,"эта ссылка отправит вас на первую страницу."+"\n"+"-"*10+"\n"+urll+"\n"+"-"*10)
            pg += 1
            req = requests.get(urll)
            soup = BeautifulSoup(req.text, "html.parser")
            
            for t in PRICE_TYPE:
                price = soup.find_all("span", class_=t)
                bot.send_message(callback.message.chat.id,PRICE_TYPE_NAME[PRICE_TYPE.index(t)])
                stroke = ""
                for data in price:
                    stroke+=str(price.index(data) + 1)+data.text[5::]+"\n"
                bot.send_message(callback.message.chat.id,stroke)
            if pg<page:
                menu_next(callback.message)
            else:
                menu_end(callback.message)
            


        for q in QUALITY:
            if callback.data == q:
                url+= "%28" + callback.data.replace(" ","%20") + "%29"
                get_text = True
                bot.send_message(callback.message.chat.id,"Введите имена стикеров:")

       
        for tip in CATEGORY:
            if callback.data == tip:
                menu_guns(callback.message,callback.data)
            
            for gun in GUNS[tip]:
                if callback.data == gun:
                    menu_skins(callback.message,tip,gun)
                    url = url + callback.data.replace(" ","%20") + "%20"
                for skin in GUNS[tip][gun]:
                    if callback.data == skin:
                        menu_quality(callback.message,callback.data)
                        url+= "%7C%20" + callback.data.replace(" ","%20") + "%20"
    
    @bot.message_handler(func=lambda message: message.text == 'Парсинг!')
    def menu_category(message):
        markup = types.InlineKeyboardMarkup()
        for tip in CATEGORY:
            markup.add(types.InlineKeyboardButton(tip,callback_data=tip))
        bot.reply_to(message, "Выберите тип оружия:",reply_markup=markup)

    def menu_guns(message,tmp):
        markup = types.InlineKeyboardMarkup()
        for gun in GUNS[tmp]:
            markup.add(types.InlineKeyboardButton(gun,callback_data=gun))
        bot.reply_to(message, "Выберите оружие:",reply_markup=markup)
    
    def menu_skins(message,tmp,tmp2):
        markup = types.InlineKeyboardMarkup()
        for skin in GUNS[tmp][tmp2]:
            markup.add(types.InlineKeyboardButton(skin,callback_data=skin))
        bot.reply_to(message, "Выберите скин:",reply_markup=markup)

    def menu_quality(message,tmp):
        markup = types.InlineKeyboardMarkup()
        for q in QUALITY:
            markup.add(types.InlineKeyboardButton(q,callback_data=q))
        bot.reply_to(message, "Выберите качество:",reply_markup=markup)

    def menu_next(message):
        markup = types.InlineKeyboardMarkup()
        markup.add(types.InlineKeyboardButton("Далее",callback_data="Далее"))
        bot.reply_to(message, "нажмите 'Далее', чтобы продолжить.",reply_markup=markup)
        
    def menu_end(message):
        bot.send_message(message.chat.id,"конец списка.")