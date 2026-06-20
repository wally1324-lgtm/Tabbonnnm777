import logging
from telegram.ext import Application, CommandHandler

from config import TOKEN
from handlers import start, status, trade, reset, history

logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO
)

def main():
    app = Application.builder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("status", status))
    app.add_handler(CommandHandler("trade", trade))
    app.add_handler(CommandHandler("reset", reset))
    app.add_handler(CommandHandler("history", history))

    print("Bot avviato...")
    app.run_polling()

if __name__ == "__main__":
    main()
