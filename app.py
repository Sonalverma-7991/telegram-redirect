from flask import Flask, redirect

app = Flask(__name__)

TELEGRAM_LINK = "https://t.me/legacytradingfemme"

@app.route('/join-trading')
def redirect_to_telegram():
    return redirect(TELEGRAM_LINK)
