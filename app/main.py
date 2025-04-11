import telebot
from dotenv import load_dotenv
import os
from handlers import register_handlers
from flask import Flask, request

# Загрузка переменных окружения
load_dotenv()
bot_token = os.getenv('TELEBOT_TOKEN')
bot = telebot.TeleBot(bot_token)
register_handlers(bot)  # Регистрируем обработчики

app = Flask(__name__)

# Установка вебхука при первом запуске
@app.route("/", methods=['GET'])
def webhook():
    bot.remove_webhook()
    bot.set_webhook(url="https://odd-mails-flow.loca.lt/" + bot_token)
    return "!", 200

# Установка вебхука
@app.route('/' + bot_token, methods=['POST'])
def getMessage():
    bot.process_new_updates([telebot.types.Update.de_json(request.stream.read().decode("utf-8"))])
    return "!", 200

if __name__ == "__main__":
    app.run(host="localhost", port=5000) # Слушаем 5000 порт
