
from aiogram import Bot, Dispatcher, executor, types
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
    executor.start_polling(dp, skip_updates=True)


