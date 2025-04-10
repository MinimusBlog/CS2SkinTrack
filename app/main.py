import os,logging,telebot
from dotenv import load_dotenv
from flask import Flask, request
from handlers import register_handlers

# Настройка логирования
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger()

# Загрузка переменных окружения из .env файла
load_dotenv()
bot_token = os.getenv('TOKEN_D')

app = Flask(__name__)
bot = telebot.TeleBot(bot_token)

register_handlers(bot)# Регистрация обработчиков

# Установка вебхука
@app.route('/' + bot_token, methods=['POST'])
def getMessage():
    bot.process_new_updates([telebot.types.Update.de_json(request.stream.read().decode("utf-8"))])
    return "!", 200

# Установка вебхука при первом запуске
@app.route("/")
def webhook():
    bot.remove_webhook()
    bot.set_webhook(url="https://62bc-75-128-244-42.ngrok-free.app/" + bot_token)
    return "!", 200

#if __name__ == "__main__":
#    app.run(host="localhost", port=5000)  # Запуск на порту 5000
bot.infinity_polling()