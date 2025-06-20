import os
import time
import requests
import random

# Clear terminal and show Banner
os.system("clear")
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

# Show Menu
print("\n[1] Method 1: ID Cloning")
print("[2] Method 2: Token Grabber")
print("[3] Method 3: Business API Clone")
print("[4] Method 4: UID List Clone")
method = input("\n[+] Select Method: ")

# Fake Facebook ID & password generator
def fake_fb_info():
    ids = ["10009" + str(random.randint(1000000000, 9999999999)) for _ in range(10)]
    passwords = ["@123456", "@2025fb", "@password1", "@freefire", "@bd786", "@iloveyou", "@admin123", "@forhad"]
    return random.choice(ids), random.choice(passwords)

def waitline(msg):
    print(msg)
    time.sleep(random.uniform(0.6, 1.4))

if method == "1":
    id, pw = fake_fb_info()
    print(f"[FACEBOOK] ID: {id} | PASS: {pw}")
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
        time.sleep(1.2)
    waitline("[✓] All Done!")

else:
    print("[-] Invalid Method Selected.")
