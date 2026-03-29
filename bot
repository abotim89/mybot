import logging
import os
from dotenv import load_dotenv
from telegram import Update
from telegram.ext import (
    Application,
    CommandHandler,
    ContextTypes,
    filters,
)

load_dotenv()

logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO,
)
logger = logging.getLogger(__name__)

BOT_TOKEN = os.getenv("BOT_TOKEN")

# ==============================
# رسائل البوت (عربي / إنجليزي)
# ==============================
MSG = {
    "start_private": (
        "👋 *مرحباً!* أنا بوت أسعار الصرف.\n"
        "سأبقيك على اطلاع دائم بأحدث أسعار الدولار وغيره.\n\n"
        "اكتب /help لرؤية الأوامر المتاحة.\n\n"
        "---\n\n"
        "👋 *Hello!* I'm your currency exchange bot.\n"
        "I'll keep you updated with the latest USD rates.\n\n"
        "Type /help to see available commands."
    ),
    "start_group": (
        "👋 *مرحباً بالجميع!*\n"
        "تمت إضافتي إلى هذه المجموعة. سأرسل تحديثات أسعار الصرف هنا.\n\n"
        "اكتب /help لرؤية الأوامر المتاحة.\n\n"
        "---\n\n"
        "👋 *Hello everyone!*\n"
        "I've been added to this group. I'll send exchange rate updates here.\n\n"
        "Type /help to see available commands."
    ),
    "help": (
        "📋 *الأوامر المتاحة:*\n\n"
        "• /start — تشغيل البوت\n"
        "• /help — عرض هذه القائمة\n"
        "• /rate — سعر الصرف الحالي _(قريباً)_\n"
        "• /summary — ملخص يومي _(قريباً)_\n\n"
        "🌍 يعمل البوت في الدردشات الخاصة والمجموعات.\n\n"
        "---\n\n"
        "📋 *Available Commands:*\n\n"
        "• /start — Start the bot\n"
        "• /help — Show this menu\n"
        "• /rate — Current exchange rate _(coming soon)_\n"
        "• /summary — Daily summary _(coming soon)_\n\n"
        "🌍 Works in private chats and groups."
    ),
    "coming_soon": (
        "⏳ هذه الميزة قيد التطوير، ستكون متاحة قريباً!\n\n"
        "---\n\n"
        "⏳ This feature is under development, coming soon!"
    ),
}

# ==============================
# معالجات الأوامر
# ==============================

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """يرد على /start بشكل مختلف حسب نوع المحادثة."""
    is_group = update.effective_chat.type in ["group", "supergroup"]
    msg = MSG["start_group"] if is_group else MSG["start_private"]
    await update.message.reply_text(msg, parse_mode="Markdown")
    logger.info(
        f"/start from {'group' if is_group else 'private'} "
        f"chat_id={update.effective_chat.id} "
        f"user={update.effective_user.username}"
    )


async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """يعرض قائمة الأوامر."""
    await update.message.reply_text(MSG["help"], parse_mode="Markdown")


async def coming_soon(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """رسالة مؤقتة للأوامر القادمة."""
    await update.message.reply_text(MSG["coming_soon"], parse_mode="Markdown")


# ==============================
# نقطة الدخول الرئيسية
# ==============================

def main() -> None:
    if not BOT_TOKEN:
        logger.error("❌ BOT_TOKEN غير موجود! أضفه في ملف .env")
        raise ValueError("BOT_TOKEN is missing. Please set it in your .env file.")

    app = Application.builder().token(BOT_TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("help", help_command))
    app.add_handler(CommandHandler("rate", coming_soon))
    app.add_handler(CommandHandler("summary", coming_soon))

    logger.info("✅ البوت يعمل... | Bot is running...")
    app.run_polling(allowed_updates=Update.ALL_TYPES)


if __name__ == "__main__":
    main()
