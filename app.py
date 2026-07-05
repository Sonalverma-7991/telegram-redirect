from flask import Flask
import telebot
import threading

app = Flask(__name__)

# --- YAHAN APNA TOKEN DAALEIN ---
TOKEN = "8336641602:AAHgupFEkMwm1M_g81jfXB1qWkj3KSNuhd8"
bot = telebot.TeleBot(TOKEN)

# Aapka XM Affiliate Link
XM_LINK = "https://www.xm.com/register/profile-account?utm_source=android-app:%2F%2Fcom.google.android.googlequicksearchbox%2F&utm_content=1280834&utm_medium=affiliate&clickid=c913dbb4-4147-4a73-99d6-840db21d51d8"

@bot.message_handler(commands=['start'])
def send_welcome(message):
    text = f"Welcome! VIP Trading group me add hone ke liye:\n\nStep 1: Is link par click karke naya XM account banayein:\n{XM_LINK}\n\nStep 2: Account banne ke baad, apna XM Account ID yahan reply me bhejein."
    bot.reply_to(message, text)

@bot.message_handler(func=lambda msg: True)
def handle_id(message):
    bot.reply_to(message, "✅ Aapki ID mil gayi hai! Hum ise verify kar rahe hain. Sahi hone par aapko isi chat mein VIP group ka link mil jayega.")

def run_bot():
    bot.infinity_polling()

# Bot ko start karna
threading.Thread(target=run_bot, daemon=True).start()

@app.route('/')
def home():
    return "Bot is running perfectly!"
