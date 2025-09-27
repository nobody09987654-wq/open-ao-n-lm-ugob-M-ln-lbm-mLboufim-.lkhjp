import requests
from telegram.ext import Updater, MessageHandler, Filters, CommandHandler

# 🔹 Bu joylarni o'zingizniki bilan almashtiring:
TELEGRAM_BOT_TOKEN = "8487100207:AAHkto2fdmSd19Rxyglcy5ldNe5vGvXiQ4Y"
DEEPSEEK_API_KEY = "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"

API_URL = "https://api.deepseek.com/chat/completions"  # kerak bo‘lsa o‘zgartirasiz
MODEL_NAME = "deepseek-r1"  # model nomi shu bo‘lsa

def start(update, context):
    update.message.reply_text("Hi,How Can I help you?")

def chat_with_deepseek(user_text):
    headers = {
        "Authorization": f"Bearer {DEEPSEEK_API_KEY}",
        "Content-Type": "application/json"
    }
    payload = {
        "model": MODEL_NAME,
        "messages": [
            {"role": "user", "content": user_text}
        ]
    }
    response = requests.post(API_URL, headers=headers, json=payload)
    result = response.json()
    return result["choices"][0]["message"]["content"]

def handle_message(update, context):
    user_text = update.message.text
    reply_text = chat_with_deepseek(user_text)
    update.message.reply_text(reply_text)

def main():
    updater = Updater(TELEGRAM_BOT_TOKEN, use_context=True)
    dp = updater.dispatcher

    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(MessageHandler(Filters.text & ~Filters.command, handle_message))

    updater.start_polling()
    updater.idle()

if __name__ == "__main__":
    main()
