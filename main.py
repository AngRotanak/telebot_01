
from aiogram import Bot, Dispatcher, executor, types
from telegram.ext import Updater, CommandHandler, CallbackContext, updater

from config import TOKEN, PORT


bot = Bot(token=TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands=['all', 'ពត៌មាន'])
async def send_welcome(message: types.Message):
    """
    This handler will be called when user sends `/start` or `/help` command
    """
    await message.reply(
        "/start \n"
        "/help \n"
        "/menu \n"
        "/order \n"
    )



if __name__ == '__main__':
    updater = Updater(TOKEN)

    dp = updater.dispatcher
    executor.start_polling(dp, skip_updates=True)
    updater.start_webhook("0.0.0.0", PORT, TOKEN, webhook_url='https://naktabot.herokuapp.com/'+TOKEN)

