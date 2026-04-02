import random
from telegram import Update
from telegram.ext import ApplicationBuilder, MessageHandler, ContextTypes, filters

greetings = ["سلام 😄", "درود 👋", "هی 🤖"]
how_are_you = ["خوبم 😎", "عالی هستم 🔥"]
bye_msgs = ["خدافظ 👋", "بعداً میبینمت 😄"]
jokes = ["😂 طنز آماده ندارم هنوز"]

async def echo(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_text = update.message.text.lower()

    if "سلام" in user_text:
        reply = random.choice(greetings)

    elif "خوبی" in user_text or "چطوری" in user_text:
        reply = random.choice(how_are_you)

    elif "بای" in user_text:
        reply = random.choice(bye_msgs)

    elif "joke" in user_text:
        reply = random.choice(jokes)

    else:
        reply = f"گفتی: {user_text}"

    await update.message.reply_text(reply)

TOKEN = "YOUR_BOT_TOKEN_HERE"

app = ApplicationBuilder().token(TOKEN).build()

app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, echo))

print("Bot is running...")

app.run_polling()
