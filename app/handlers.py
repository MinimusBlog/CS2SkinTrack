from telebot import types
import logging

# Настройка логирования
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger()

def register_handlers(bot):
    @bot.message_handler(commands=['start'])
    def start_message(message):
        logger.info(f"Отправка /start {message.chat.id}")
        # Создание клавиатуры
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
        item1 = types.KeyboardButton("Помощь")  # Кнопка "Помощь"
        item2 = types.KeyboardButton("Конвертация в USDT")  # Кнопка "Настройки"
        markup.add(item1, item2)  # Добавляем кнопки в клавиатуру
        bot.send_message(message.chat.id, 'Привет! Выберите действие:', reply_markup=markup)

    @bot.message_handler(func=lambda message: message.text == 'Помощь')
    def help_message(message):
        logger.info(f"Отправка помощи {message.chat.id}")
        instructions = """
        Инструкция по использованию бота:
        1. Выберите действие из меню.
        2. Следуйте инструкциям на экране.
        """
        bot.send_message(message.chat.id, instructions)