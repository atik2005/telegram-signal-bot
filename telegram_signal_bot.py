import time
import requests
from datetime import datetime
import random

BOT_TOKEN = '7811319089:AAGcAvtvT4CrPDxvT6xtgTkQ-VnbCAvMqZQ'
CHAT_ID = '-1002806211493'  # তোমার গ্রুপ আইডি

def send_signal():
    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    result = random.choice(["Big", "Small"])
    message = f"""🎯 DK WIN 1-Minute AI Signal 🎯

⏰ Time: {current_time}
🔎 Result: 🔶 {result}

📝 Register & Play Now:
👉 Click Here to Register (27718100924) রেফার লিংক

🧑‍💻 Creator: @BABY_CODER_1"""

    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    data = {
        "chat_id": CHAT_ID,
        "text": message
    }
    requests.post(url, data=data)

while True:
    send_signal()
    print("✅ Message sent at", datetime.now())
    time.sleep(60)
