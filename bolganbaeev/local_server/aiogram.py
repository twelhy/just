from aiogram import Bot, Dispatcher, executor, types

bot = Bot('7105666030:AAE-YdgolF4eifV1GH-T1m-PEBC1-PlacvE')
dp = Dispatcher(bot)

@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    #await bot.send_message(message.chat.id, 'Hello')
    #await  message.answer('Hello')
    #await message.reply('Hello')



executor.start_polling(dp)
