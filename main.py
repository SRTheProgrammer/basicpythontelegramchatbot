import Constants as keys
from telegram.ext import *

import Responses as R

print("Bot Started Successfully...")

def start_command(update, context):
    update.message.reply_text('Type something like hi or hello to get started.')

def help_command(update, context):
    update.message.reply_text('if You Need any Help Ask it On google.com')

def handle_message(update, context):
    text = str(update.message.text).lower()
    response = R.sample_responses(input_text=text)

    update.message.reply_text(response)

def error(update, context):
    print(f"Update {update} caused error {context.error}")

def main(update, context):
    updater = Updater(keys.BOT_TOKEN, use_context=True)
    dp = updater.dispatcher

    dp.add_handler(CommandHandler("start", start_command))
    dp.add_handler(CommandHandler("help", help_command))

    dp.add_handler(MessageHandler(Filters.text, handle_message))

    dp.add_error_handler(error)

    updater.start_polling()
    updater.idle()


main(None, None)







