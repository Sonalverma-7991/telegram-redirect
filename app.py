from flask import Flask
import telebot
import threading

app = Flask(__name__)

# Your Bot Token
TOKEN = "8890468186:AAEEDaUa2cMZkLgS_b_rt7JfIz3eCnjgdk"
bot = telebot.TeleBot(TOKEN)

# Your Affiliate Links
XM_LINK = "https://www.xm.com/register/profile-account?utm_source=android-app:%2F%2Fcom.google.android.googlequicksearchbox%2F&utm_content=1280834&utm_medium=affiliate&clickid=c913dbb4-4147-4a73-99d6-840db21d51d8"
DELTA_LINK = "https://www.delta.exchange/?code=IPURND"

# Your VIP Group Link
VIP_GROUP_LINK = "https://t.me/fmevaulthq"

@bot.message_handler(commands=['start'])
def send_welcome(message):
    text = f"Welcome! To join our VIP Trading group:\n\nStep 1: Please create a new account on EITHER XM or Delta Exchange using the links below:\n\nOption A (XM Broker):\n{XM_LINK}\n\nOption B (Delta Exchange):\n{DELTA_LINK}\n\nStep 2: After creating your account, reply to this message with your Registered Email ID to get the VIP link."
    bot.reply_to(message, text)

@bot.message_handler(func=lambda msg: True)
def give_vip_link(message):
    reply_text = f"✅ Thank you for providing your details!\n\nHere is your exclusive link to join the VIP Group:\n👉 {VIP_GROUP_LINK}\n\nWelcome to the team!"
    bot.reply_to(message, reply_text)

def run_bot():
    bot.infinity_polling()

# Start the bot
threading.Thread(target=run_bot, daemon=True).start()

@app.route('/')
def home():
    return "Bot is running perfectly with both XM and Delta Exchange!"
