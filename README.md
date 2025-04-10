# CS2SkinTrack

### Установка зависимостей:
- **Создание виртуального окружения**: Команда `python -m venv .venv` создает новое виртуальное окружение в директории `.venv`
- **Активация**: Команда активации на Windows используется `.venv\Scripts\activate`, а на macOS/Linux — `.venv\bin/activate`

- **dotenv**: Хранение токена бота `pip install python-dotenv`
- **Telebot**: Библиотека для создания бота `pip install pyTelegramBotAPI`
- **BeautifulSoup4**: Древо HTML `pip install beautifulsoup4`
- **requests**: HTTP `pip install requests`
- **Flask**: WebHooks `pip install Flask`

- **list**: Проверка установленных зависимостей `pip list`

### Запуск
-  `python app/main.py`

[Ngrok](https://ngrok.com/)
You must be logged in to ngrok

Click on the tab for your token

Next, run the .exe

Paste your token

```
#Set port
ngrok http 5000
```
Next, copy forwarding link

Paste the link into a webhook .py file

```
#run the .py file
python main.py
```

Open the link in browser

Next, click on visit site

Done, if you see '!'