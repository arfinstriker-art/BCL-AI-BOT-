import os
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters, ContextTypes
from openai import OpenAI

# 🔑 TOKEN (এখানে তোমার BotFather token বসাও)
BOT_TOKEN = "8737522075:AAHjTAOU_k5I_BTKIQJE1qfeYvfY1unXO6k"

# 🤖 OpenAI Client
client = OpenAI(api_key="YOUR_OPENAI_API_KEY")

# 😎 Bot personality
SYSTEM_PROMPT = """
You are a funny, slightly sarcastic AI bot from Bangladesh Cyber Legion.
You talk with attitude 😎, use emojis 🔥, sometimes roast users 😏 but never too offensive.
Keep replies short, fun, and engaging.
"""

# 🚀 Start command
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = """
🤖 Welcome bro 😎🔥

আমি Bangladesh Cyber Legion এর AI Bot 💥  
কথা বল, মজা কর, info নাও 😏

━━━━━━━━━━━━━━━━━━━
💬 Chat | 😂 Fun | 📚 Help | 👥 Team Info

🚀 Team join করতে চাও?
👉 CEO: @striker_arfin104

⚠️ Respect দিলে respect পাবে ❤️
━━━━━━━━━━━━━━━━━━━

চলো শুরু করি 🚀
"""
    await update.message.reply_text(text)

# 💬 Reply system
async def reply(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_msg = update.message.text

    try:
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": SYSTEM_PROMPT},
                {"role": "user", "content": user_msg}
            ]
        )

        bot_reply = response.choices[0].message.content
        await update.message.reply_text(bot_reply)

    except Exception as e:
        await update.message.reply_text("⚠️ Error: " + str(e))

# ▶️ Run bot
app = ApplicationBuilder().token(BOT_TOKEN).build()

app.add_handler(CommandHandler("start", start))
app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, reply))

print("Bot is running...")
app.run_polling()
