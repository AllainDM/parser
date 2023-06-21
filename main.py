from datetime import datetime
import requests
import os

from aiogram import Bot, Dispatcher, executor, types

import config

# session = requests.Session()

# bot = Bot(token=config.BOT_API_TOKEN, parse_mode=types.ParseMode.HTML)
bot = Bot(token=config.BOT_API_TOKEN)
dp = Dispatcher(bot)

url_drive2 = "https://www.skoda-piter.ru/forum/"

HEADERS = {
    "main": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:105.0) Gecko/20100101 Firefox/105.0"
}


@dp.message_handler(commands=['0'])
async def echo_mess(message: types.Message):
    answer = get_html_drive2(url_drive2)
    await bot.send_message(message.chat.id, answer)
    print("Сообщение отправлено")


def get_html_drive2(url):
    # html = session.get(url)
    response_url_drive2 = requests.get(url_drive2)
    print(response_url_drive2)
    answer = "Тут будет ответ от drive2.ru"  # Ответ боту
    if response_url_drive2.status_code == 200:
        print("Страничка Drive2.ru получена")
    else:
        print("Судя по всему страничка не скачана")
    return answer


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
