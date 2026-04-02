from telegram import Update
from telegram.ext import ApplicationBuilder, MessageHandler, filters, ContextTypes
import random

# جواب‌ها
greetings = ["سلام 😄", "هی رفیق 👋", "خوش آمدی دلاور 😊"]
how_are_you = ["خوبم مرسی 😎", "عالی‌ام 😁", "تو خوبی؟ 😉"]
bye_msgs = ["خداحافظ 👋", "بعداً میبینمت 😄", "مواظب خودت باش ❤️"]
jokes = [
    "برنامه‌نویس بدون قهوه یعنی هیچی ☕😂",
    "یه باگ داشتم، الان دو تا شده 🤣",
    "زندگی مثل کده... همیشه یه ارور داره 😅"
]

# تابع اصلی


async def echo(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_text = update.message.text.lower()

    if "سلام" in user_text:
        reply = random.choice(greetings)

    elif "خوبی" in user_text or "چطوری" in user_text:
        reply = random.choice(how_are_you)

    elif "خداحافظ" in user_text or "بای" in user_text:
        reply = random.choice(bye_msgs)

    elif "جوک" in user_text:
        reply = random.choice(jokes)

    else:
        reply = f"😄 گفتی: {user_text}"

    await update.message.reply_text(reply)


# 🔴 اینجا توکن رباتتو بذار
TOKEN = "8217901668:AAGM-ysVz2KSNIMlhYu7tOySLf8QDfqdZAA"

# ساخت ربات
app = ApplicationBuilder().token(: AAGM-ysVz2KSNIMlhYu7tOySLf8QDfqdZAA).build()

# هندل پیام‌ها
app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, echo))

# اجرا (بدون ارور)
print("ربات روشن شد 🚀")
app.run_polling(close_loop=False)
