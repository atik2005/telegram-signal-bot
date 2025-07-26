import time
import requests
from datetime import datetime
import random

# ✅ তোমার টেলিগ্রাম বটের টোকেন ও চ্যাট আইডি
BOT_TOKEN = '7811319089:AAGcAvtvT4CrPDxvT6xtgTkQ-VnbCAvMqZQ'
CHAT_ID = '-1002806211493'  # তোমার গ্রুপ আইডি

# ✅ মেসেজ সেন্ড করার ফাংশন
def send_message(message):
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    data = {
        "chat_id": CHAT_ID,
        "text": message,
        "parse_mode": "HTML"
    }
    try:
        response = requests.post(url, data=data)
        if response.status_code == 200:
            print("✅ Message sent:", message[:20])
        else:
            print("❌ Failed to send message:", response.text)
    except Exception as e:
        print("❌ Error:", e)

# ✅ সিগনাল পাঠানোর ফাংশন
def send_signal():
    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    result = random.choice(["Big", "Small"])
    message = f"""🎯 DK WIN 1-Minute AI Signal 🎯

⏰ Time: {current_time}
🔎 Result: 🔶 {result}

📝 Register & Play Now:
👉 <a href="https://dkwin9.com/#/register?invitationCode=27718100924">Click Here to Register</a>

🧑‍💻 Creator: @BABY_CODER_1"""
    send_message(message)

# ✅ সিগনালের পরে 🤑 ইমোজি পাঠানো
def send_emojis(count=3, delay=10):
    for i in range(count):
        time.sleep(delay)
        send_message("🤑")

# ✅ লুপ চালানো
try:
    while True:
        send_signal()
        send_emojis(count=3, delay=10)
        # সিগনাল + ৩টি ইমোজি = মোট ৩০ সেকেন্ড। তাই ৩০ সেকেন্ড অপেক্ষা করে আবার শুরু
        time.sleep(30)
except KeyboardInterrupt:
    print("🛑 Bot manually stopped.")
