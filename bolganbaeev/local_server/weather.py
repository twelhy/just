#https://api.openweathermap.org/data/2.5/weather?q=NewYork&appid=fb9e3f0b3b3b2283a3c87a9dbf283359units=metric
import telebot
import requests
import json

bot = telebot.TeleBot('7105666030:AAE-YdgolF4eifV1GH-T1m-PEBC1-PlacvE')
API = 'fb9e3f0b3b3b2283a3c87a9dbf283359'

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, 'I\'glad to see you! write city name')


@bot.message_handler(content_types=['text'])
def get_weather(message):
    city = message.text.strip().lower()
    res = requests.get(f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API}&units=metric')
    if res.status_code == 200:
        data = json.loads(res.text)
        #dataa = json.loads(data.get("weather").list)
        bot.reply_to(message, f'Weather: {data.get("weather")[0].get("main")} \nTemperature: {data["main"]["temp"]}°C\nWind: {data.get("wind").get("speed")}m/s')
    else:
        bot.reply_to(message, 'The city is incorrectly specified')
bot.polling(none_stop=True)