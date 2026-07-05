from flask import Flask
import telebot
import threading

app = Flask(__name__)

# --- YAHAN APNA TOKEN DAALEIN ---
TOKEN = "YAHAN_BOTFATHER_WALA_TOKEN_PASTE_KAREIN"
bot = telebot.TeleBot(TOKEN)

# Aapka XM Affiliate Link
XM_LINK = "https://www.xm.com/register/profile-account?utm_source=android-app:%2F%2Fcom.google.android.googlequicksearchbox%2F&utm_content=1280834&utm_medium=affiliate&clickid=c913dbb4-4147-4a73-99d6-840db21d51d8"

@bot.message_handler(commands=['start'])
def send_welcome(message):
    text = f"Welcome! To join our VIP Trading group:\n\nStep 1: Please create a new XM account by clicking this link:\n{XM_LINK}\n\nStep 2: After creating the account, reply to this message with your XM Account ID or Registered Email."
    bot.reply_to(message, text)

@bot.message_handler(func=lambda msg: True)
def handle_id(message):
    bot.reply_to(message, "✅ Your details have been received! We are currently verifying your account. Once successfully verified, you will receive the VIP group link in this chat shortly.")

def run_bot():
    bot.infinity_polling()

# Bot ko start karna
threading.Thread(target=run_bot, daemon=True).start()

@app.route('/')
def home():
    return "Bot is running perfectly!"
