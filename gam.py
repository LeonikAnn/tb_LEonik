# 5838487633:AAE30cv_DKGro6LzvhfOEjvR8DvAqqXGNaA
import telebot
from telebot import types
import requests
import json
from pprint import pprint

open_weather_token = 'b504c067a7b2095dcc1641a77866dff2'
token = '5838487633:AAE30cv_DKGro6LzvhfOEjvR8DvAqqXGNaA'
bot = telebot.TeleBot(token)


def create_keyboard():
    keyboard = types.InlineKeyboardMarkup()
    drink_btn = types.InlineKeyboardButton(text='Хочу пить', callback_data='1')
    eat_btn = types.InlineKeyboardButton(text='Хочу eсть', callback_data='2')
    walk_btn = types.InlineKeyboardButton(text='Хочу гулять', callback_data='3')
    sleep_btn = types.InlineKeyboardButton(text='Хочу спать', callback_data='4')
    joke_btn = types.InlineKeyboardButton(text='Хочу шутку', callback_data='5')
    # forecast_btn = types.InlineKeyboardButton(text='Прогноз погоды', callback_data='6')
    keyboard.add(drink_btn, eat_btn, walk_btn, sleep_btn, joke_btn, forecast_btn)
    return keyboard


@bot.message_handler(commands=['start', 'старт', 'поехали'])
def start_bot(message):
    klava = create_keyboard()
    bot.send_message(message.chat.id, 'Добрый день! Выберите что хотите.',
                     reply_markup=klava)


@bot.callback_query_handler(func=lambda call: True)
def callback(call):
    if call.message:
        if call.data == '1':
            img = open('photo_2023-01-16_20-24-07.jpg', 'rb')
            bot.send_photo(
                chat_id=call.message.chat.id,
                photo='https://st.depositphotos.com/1741875/1274/i/450/depositphotos_12747823-stock-photo-pouring-water-on-a-glass.jpg',
                caption='суточная норма воды 2л',
                reply_markup=create_keyboard()
            )
            img.close()
        if call.data == '2':
            img = open('photo_2023-01-16_20-23-07.jpg', 'rb')
            bot.send_photo(
                chat_id=call.message.chat.id,
                photo='https://klike.net/uploads/posts/2019-06/1559545617_2.jpg',
                caption='Пупсик, Биосистема',
                reply_markup=create_keyboard()
            )
            img.close()
        if call.data == '3':
            bot.send_photo(
                chat_id=call.message.chat.id,
                photo='https://medaboutme.ru/upload/medialibrary/490/medaboutme_shutterstock_402920080.jpg',
                caption='Хорошей прогулки, друг!',
                reply_markup=create_keyboard()
            )
        if call.data == '4':
            bot.send_photo(
                chat_id=call.message.chat.id,
                photo='https://incrussia.ru/wp-content/uploads/2019/11/iStock-896820002-1.jpg',
                caption='Сладких снов)',
                reply_markup=create_keyboard()
            )

        if call.data == '5':
            bot.send_photo(
                chat_id=call.message.chat.id,
                photo='https://kartinkof.club/uploads/posts/2022-03/1648385813_1-kartinkof-club-p-mem-ya-chto-dlya-tebya-shutka-1.jpg',
                caption='М?!',
                reply_markup=create_keyboard()
            )
#         if call.data == '6':
#             def get_weather():
#                 base_url = "https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={API key}"
#                 URL = urls
#                 res = requests.get(urls)
#                 if res.status_code == 200:
#                     data = res.json()
#                     temp = int(data['main']['temp'] - 273.15)
#                     print(data)
#                 else:
#                     print(' Error in HTTP')
#             get_weather()
# #
# open_weather_token = 'b504c067a7b2095dcc1641a77866dff2'
# city = 'warsaw'
# header = {'https://api.openweathermap.org/data/2.5/weather?lat={city}&appid={open_weather_token}'}
# urls = 'https://openweathermap.org/city/756135'
# r = requests.get(urls)
# data = r.json()
# pprint(data)


bot.polling(non_stop=True)
