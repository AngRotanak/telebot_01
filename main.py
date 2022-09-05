from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext

from config import TOKEN


def start(update:Updater, context:CallbackContext):
    update.message.reply_text("Hey {}".format(update.message.from_user.username))

if __name__ == '__main__':
    updater = Updater(TOKEN)

    dp = updater.dispatcher

    dp.add_handler(CommandHandler("start", start))

    updater.start_polling()
    updater.idle()