from telebot import types
import logging
import json
import os

# Настройка логирования
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger()

# Загрузка данных из json
with open(os.path.join(os.path.dirname(__file__), 'data.json'), 'r', encoding='utf-8') as f:
    data = json.load(f)

CATEGORY = data["CATEGORY"]
GUNS = data["GUNS"]

def register_handlers(bot):
    @bot.message_handler(commands=['start'])
    def start_message(message):
        logger.info(f"Отправка /start {message.chat.id}")
        # Создание клавиатуры
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
        item1 = types.KeyboardButton("Помощь")  # Кнопка "Помощь"
        item2 = types.KeyboardButton("Конвертация в USDT")  # Кнопка "Конвертация"
        item3 = types.KeyboardButton("Выбрать оружие")  # Кнопка "Выбор оружия"
        markup.add(item1, item2, item3)  # Добавляем кнопки в клавиатуру
        bot.send_message(message.chat.id, 'Привет! Выберите действие:', reply_markup=markup)

    @bot.message_handler(func=lambda message: message.text == 'Выберите оружие')
    def choose_weapon(message):
        logger.info(f"Пользователь {message.chat.id} выбрал 'Выберите оружие'")
        
        markup = types.InlineKeyboardMarkup()
        for category in CATEGORY:
            markup.add(types.InlineKeyboardButton(category, callback_data=f"category:{category}"))
        bot.send_message(message.chat.id, "Выберите тип оружия:", reply_markup=markup)

    @bot.callback_query_handler(func=lambda callback: callback.data.startswith("category:"))
    def show_weapons(callback):
        category = callback.data.split(":")[1]
        logger.info(f"Пользователь {callback.message.chat.id} выбрал категорию {category}")

        markup = types.InlineKeyboardMarkup()
        for gun in GUNS.get(category, []):
            markup.add(types.InlineKeyboardButton(gun, callback_data=f"gun:{gun}"))
        bot.edit_message_text(chat_id=callback.message.chat.id, message_id=callback.message.message_id,
                              text=f"Вы выбрали категорию: {category}. Теперь выберите оружие:",
                              reply_markup=markup)

    @bot.callback_query_handler(func=lambda callback: callback.data.startswith("gun:"))
    def weapon_selected(callback):
        gun = callback.data.split(":")[1]
        logger.info(f"Пользователь {callback.message.chat.id} выбрал оружие {gun}")
        bot.send_message(callback.message.chat.id, f"Вы выбрали оружие: {gun}")