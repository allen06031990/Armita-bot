import telebot
from telebot import types

# 👉 Put your NEW token here
TOKEN = os.environ["BOT_TOKEN"]

bot = telebot.TeleBot(TOKEN)

# Price in Stars (you can change this)
PRICE = 1000

@bot.message_handler(commands=['start'])
def welcome(message):
    markup = types.InlineKeyboardMarkup()
    btn = types.InlineKeyboardButton(f"Pay {PRICE} Stars ⭐", callback_data="pay")
    markup.add(btn)

    text = (
        "Hey dirty boy 😈\n\n"
        "You found me from xHamster...\n"
        "Ready for something private?\n\n"
        f"Pay {PRICE} Stars to unlock exclusive access & private chats with me 🔥"
    )
    bot.send_message(message.chat.id, text, reply_markup=markup)

@bot.callback_query_handler(func=lambda call: call.data == "pay")
def send_payment(call):
    prices = [types.LabeledPrice(label="Private Access with Armita", amount=PRICE)]

    bot.send_invoice(
        chat_id=call.message.chat.id,
        title="Private Access 🔥",
        description="Unlock exclusive content & private chats with Armita",
        invoice_payload="private_access",
        provider_token="",          # Keep empty for Telegram Stars
        currency="XTR",
        prices=prices
    )

@bot.pre_checkout_query_handler(func=lambda query: True)
def pre_checkout(pre_checkout_query):
    bot.answer_pre_checkout_query(pre_checkout_query.id, ok=True)

@bot.message_handler(content_types=['successful_payment'])
def payment_success(message):
    bot.send_message(
        message.chat.id,
        "✅ Payment successful!\n\n"
        "Thank you baby 🔥\n"
        "I’ll contact you soon for private access."
    )

print("Bot is running...")
bot.infinity_polling()
