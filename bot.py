import os
from telegram.ext import Updater, CommandHandler
from flask import Flask
import threading

# قراءة التوكن من Environment Variables
TOKEN = os.getenv("BOT_TOKEN")

# التأكد من وجود التوكن
if not TOKEN:
    raise ValueError("No BOT_TOKEN found in environment variables")

# إنشاء البوت
updater = Updater(TOKEN)
dispatcher = updater.dispatcher

# أمر /start
def start(update, context):
    update.message.reply_text("🤖 أهلاً! البوت يعمل بنجاح 🚀")

# إضافة الأمر
dispatcher.add_handler(CommandHandler("start", start))

# --- Flask Server ---
app = Flask(__name__)

@app.route('/')
def home():
    return "Bot is running!"

# --- تشغيل الاثنين معًا ---
def run_bot():
    updater.start_polling()
    updater.idle()

if __name__ == "__main__":
    # تشغيل البوت في Thread
    threading.Thread(target=run_bot).start()
    
    # تشغيل السيرفر (عشان Render)
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)
