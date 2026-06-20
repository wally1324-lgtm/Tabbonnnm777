from telegram import Update
from telegram.ext import ContextTypes

from trader import run_trade
from trader import portfolio


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "🤖 Trading Bot Simulato\n\n"
        "Capitale iniziale: 1000€\n\n"
        "Comandi:\n"
        "/trade → esegui simulazione\n"
        "/status → stato portafoglio\n"
        "/history → ultime operazioni\n"
        "/reset → reset portafoglio"
    )


async def trade(update: Update, context: ContextTypes.DEFAULT_TYPE):
    price, signal, amount, value = run_trade()

    # messaggio normale
    msg = (
        f"📊 Prezzo: {price}\n"
        f"📡 Segnale: {signal}\n"
        f"📦 Quantità: {amount}\n"
        f"💰 Valore Portafoglio: {value:.2f}€"
    )

    await update.message.reply_text(msg)


async def status(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        f"💰 Saldo: {portfolio.balance:.2f}€\n"
        f"📦 Posizione: {portfolio.position}\n"
        f"📊 Valore totale: {portfolio.value(1):.2f}€"
    )


async def history(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if not portfolio.history:
        await update.message.reply_text("Nessuna operazione registrata.")
        return

    text = "\n".join(portfolio.history[-10:])
    await update.message.reply_text(text)


async def reset(update: Update, context: ContextTypes.DEFAULT_TYPE):
    portfolio.balance = 1000
    portfolio.position = 0
    portfolio.history.clear()

    await update.message.reply_text("🔄 Portafoglio resettato a 1000€")
