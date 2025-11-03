```
termux-setup-storage
pkg update -y
pkg upgrade -y
pkg install -y python clang make libffi openssl pkg-config git curl wget
python -m pip install --upgrade pip setuptools wheel
python -m pip install aiohttp

git clone https://github.com/Forhadj/anyphone-hack.git
cd anyphone-hack
python sender.py
