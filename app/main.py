import os,logging,telebot
from dotenv import load_dotenv
<<<<<<< HEAD
import os
=======
>>>>>>> d10df0ad0296d1a73ddc785fd37664ab074aeb22
from flask import Flask, request
from handlers import register_handlers

# Загрузка переменных окружения из .env файла
load_dotenv()

app = Flask(__name__)
bot = telebot.TeleBot(os.getenv("TELEBOT_TOKEN"))

register_handlers(bot) # Регистрация обработчиков

bot.infinity_polling()
# Установка вебхука
@app.route('/' + bot_token, methods=['POST'])
def getMessage():
    bot.process_new_updates([telebot.types.Update.de_json(request.stream.read().decode("utf-8"))])
    return "!", 200

# Установка вебхука при первом запуске
@app.route("/")
def webhook():
    bot.remove_webhook()
    bot.set_webhook(url="https://3df4-183-96-15-159.ngrok-free.app/" + bot_token)
    return "!", 200

if __name__ == "__main__":
<<<<<<< HEAD
    app.run(host="localhost", port=5000) # Слушаем 5000 порт
=======
    app.run(host="localhost", port=5000)  # Запуск на порту 5000
bot.infinity_polling()
>>>>>>> d10df0ad0296d1a73ddc785fd37664ab074aeb22
