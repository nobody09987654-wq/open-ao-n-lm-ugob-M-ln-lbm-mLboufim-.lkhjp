import openai
from telegram.ext import Updater, MessageHandler, Filters, CommandHandler

# 🔹 Replace with your keys
TELEGRAM_BOT_TOKEN = "8487100207:AAHkto2fdmSd19Rxyglcy5ldNe5vGvXiQ4Y"
OPENAI_API_KEY = "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"

openai.api_key = OPENAI_API_KEY

def start(update, context):
    update.message.reply_text("Hello! I'm your ChatGPT-powered bot. Send me any message.")

def chat_with_gpt(text):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": text}]
    )
    return response.choices[0].message.content

def handle_message(update, context):
    user_text = update.message.text
    reply = chat_with_gpt(user_text)
    update.message.reply_text(reply)

def main():
    updater = Updater(TELEGRAM_BOT_TOKEN, use_context=True)
    dp = updater.dispatcher

    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(MessageHandler(Filters.text & ~Filters.command, handle_message))

    updater.start_polling()
    updater.idle()

if __name__ == "__main__":
    main()
