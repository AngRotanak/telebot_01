from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext, MessageHandler, Filters

from config import TOKEN, PORT


def start(update:Updater, context:CallbackContext):
    update.message.reply_text("Hey hello {} from Heroku !!".format(update.message.from_user.username))

def start(update:Updater, context:CallbackContext):
    update.message.reply_text("Help {} from Heroku !!".format(update.message.from_user.username))

if __name__ == '__main__':
    updater = Updater(TOKEN)

    dp = updater.dispatcher

    # on different commands - answer in Telegram
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("help", help))



updater.start_webhook("0.0.0.0", PORT, TOKEN, webhook_url='https://naktabot.herokuapp.com/'+TOKEN)
    updater.idle()

