# CS2SkinTrack

## Описание
CS2SkinTrack — настоящий помощник для всех, кто играет в CS2 или торгует внутриигровыми предметами на Steam! Он следит за ценами на торговой площадке Steam, так что вы всегда будете в курсе, сколько стоит тот или иной предмет.  Нужен перевод цены в другую валюту?  Без проблем!  Бот удобен для пользователей из разных стран и работает без привязки к вашему аккаунту Steam.  Сэкономьте свое время — просто задавайте вопросы боту через Telegram. Он подойдёт как опытным игрокам, так и новичкам!

### Установка
[Python](https://www.python.org/downloads/)


```sh
$ git clone https://github.com/yourusername/CS2SkinTrack.git
```

```sh
$ cd CS2SkinTrack
```

- **Создание виртуального окружения**: Команда `python -m venv .venv` создает новое виртуальное окружение в директории `.venv`
- **Активация**: Команда активации на Windows используется `.venv\Scripts\activate`, а на macOS/Linux — `.venv\bin/activate`

- **dotenv**: Хранение токена бота `pip install python-dotenv`
- **Telebot**: Библиотека для создания бота `pip install pyTelegramBotAPI`
- **BeautifulSoup4**: Древо HTML `pip install beautifulsoup4`
- **requests**: HTTP `pip install requests`
- **Flask**: WebHooks `pip install Flask`
- **DateTime**: `pip install datetime`
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

### Запуск (2 способ)

Устанавливаем
```
npm install -g localtunnel
```

Далее проверяем, что lt установился

```
npm list -g localtunnel
```

Запускаем в терминале
```
npx localtunnel --port 5000
```

Полученный url вставляем до '/' в webhook method [GET]
```
https://example.loca.lt
```

После установки, запускаем main.py
```
python app/main.py
```

Открываем localhost для запуска webhook
```
http://localhost:5000/
```

Успех! Веб-сервер запущен. 😀