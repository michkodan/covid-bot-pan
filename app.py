import requests
import json
import telebot
from telebot import apihelper
from telebot import types

apihelper.proxy = {'https': 'socks5h://185.153.198.226:50210'}

bot = telebot.TeleBot('1103844740:AAFOTC9I4JJvh8Yg5lYOJXvjztV9YQ3f62U')

url_cities = 'https://www.trackcorona.live/api/cities/'
response_cities = requests.request("GET", url_cities)
result_cities = response_cities.json()

url_countries = 'https://www.trackcorona.live/api/countries/'
response_countries = requests.request("GET", url_countries)
result_countries = response_countries.json()


@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    btn1 = types.KeyboardButton('Санкт-Петербург')
    btn2 = types.KeyboardButton('Хабаровск')
    btn3 = types.KeyboardButton('Москва')
    btn4 = types.KeyboardButton('Во всей России')
    btn5 = types.KeyboardButton('Для Катеньки❤')

    markup.add(btn1, btn2, btn3, btn4, btn5)
    send_msg = f'Привет, <b>{message.from_user.first_name}</b>!\nВыбери город: '
    bot.send_message(message.chat.id, send_msg, parse_mode='html', reply_markup=markup)
    # bot.message_handler(message.chat.id, get_message)

@bot.message_handler(content_types=['text'])
def get_message(message):
    get_message = message.text

    if get_message == 'Для Катеньки❤':
        with open('AnimatedSticker.tgs', 'rb') as f:
            return bot.send_sticker(message.chat.id, f, timeout=50).sticker

    if get_message == 'Санкт-Петербург':
        for item in result_cities['data']:
            if item['location'] == 'Saint Petersburg':
                get_message = f"<u>Данные по городу:</u>\n"\
                              f"<b>Подтверждено:</b> {item['confirmed']}\n"\
                              f"<b>Умерло:</b> {item['dead']}\n"\
                              f"<b>Выздоровело:</b> {item['recovered']}"
        bot.send_message(message.chat.id, get_message, parse_mode='html')

    if get_message == 'Хабаровск':
        for item in result_cities['data']:
            if item['location'] == 'Khabarovsk Krai':
                get_message = f"<u>Данные по городу:</u>\n"\
                              f"<b>Подтверждено:</b> {item['confirmed']}\n"\
                              f"<b>Умерло:</b> {item['dead']}\n"\
                              f"<b>Выздоровело:</b> {item['recovered']}"
        bot.send_message(message.chat.id, get_message, parse_mode='html')

    if get_message == 'Москва':
        for item in result_cities['data']:
            if item['location'] == 'Moscow':
                get_message = f"<u>Данные по городу:</u>\n"\
                              f"<b>Подтверждено:</b> {item['confirmed']}\n"\
                              f"<b>Умерло:</b> {item['dead']}\n"\
                              f"<b>Выздоровело:</b> {item['recovered']}"
        bot.send_message(message.chat.id, get_message, parse_mode='html')

    if get_message == 'Во всей России':
        for item in result_countries['data']:
            if item['location'] == 'Russia':
                get_message = f"<u>Данные по стране:</u>\n"\
                              f"<b>Подтверждено:</b> {item['confirmed']}\n"\
                              f"<b>Умерло:</b> {item['dead']}\n"\
                              f"<b>Выздоровело:</b> {item['recovered']}"
        bot.send_message(message.chat.id, get_message, parse_mode='html')

    else:
        bot.send_message(message.chat.id,
                         f'<b>{message.from_user.first_name}</b>, так-так, не нужно писать текст, пользуйся кнопками!',
                         parse_mode='html')


if __name__ == '__main__':
    bot.infinity_polling(none_stop=True)


