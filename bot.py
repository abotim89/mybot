import os
from telegram.ext import Updater, CommandHandler

TOKEN = os.getenv("BOT_TOKEN")

def start(update, context):
    update.message.reply_text("البوت يعمل بنجاح ✅")

updater = Updater(TOKEN)

dp = updater.dispatcher
dp.add_handler(CommandHandler("start", start))

updater.start_polling()
updater.idle()
