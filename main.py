from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext

from config import TOKEN, PORT


def start(update, context):
    """Send a message when the command /start is issued."""
    update.message.reply_text("OK {} I am here to help you !!".format(update.message.from_user.username))


def help(update, context):
    """Send a message when the command /help is issued."""
    update.message.reply_text("Hey hello {} from Heroku !!".format(update.message.from_user.username))


def main():
    updater = Updater(TOKEN)

    dp = updater.dispatcher

    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("help", help))




    updater.start_webhook("0.0.0.0", PORT, TOKEN, webhook_url='https://naktabot.herokuapp.com/' + TOKEN)
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()


