from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext
import os

# Çevresel değişkenden API anahtarını alın
API_KEY = os.getenv('6981545815:AAHuOOT1uBZRP5dtnuLmQAm17b-7a5r8lF4')

def start(update: Update, context: CallbackContext) -> None:
    update.message.reply_text('Merhaba! Ben sizin botunuzum.')

def main():
    updater = Updater(API_KEY)
    dispatcher = updater.dispatcher
    dispatcher.add_handler(CommandHandler("start", start))
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
