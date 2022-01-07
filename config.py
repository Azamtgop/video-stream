import os
from os import getenv
from dotenv import load_dotenv

if os.path.exists("local.env"):
    load_dotenv("local.env")

load_dotenv()
admins = {}
SESSION_NAME = getenv("SESSION_NAME", "session")
BOT_TOKEN = getenv("BOT_TOKEN")
BOT_NAME = getenv("BOT_NAME", "Video Stream")
API_ID = int(getenv("API_ID"))
API_HASH = getenv("API_HASH")
OWNER_NAME = getenv("OWNER_NAME", "cute_boy701")
ALIVE_NAME = getenv("ALIVE_NAME", "⭐🇱ᴜᴄᴋʏ ⸎🇧ᴏʏ ⭕")
BOT_USERNAME = getenv("BOT_USERNAME", "luckyvideobot")
ASSISTANT_NAME = getenv("ASSISTANT_NAME", "cute_boy701")
GROUP_SUPPORT = getenv("GROUP_SUPPORT", "terayaarhoomai")
UPDATES_CHANNEL = getenv("UPDATES_CHANNEL", "maxopeditz")
SUDO_USERS = list(map(int, getenv("SUDO_USERS", "1729094176").split()))
COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "/ ! .").split())
ALIVE_IMG = getenv("ALIVE_IMG", "https://telegra.ph/file/8c5e564422e8c5e0085ca.jpg")
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "60"))
UPSTREAM_REPO = getenv("UPSTREAM_REPO", "https://github.com/levina-lab/video-stream")
IMG_1 = getenv("IMG_1", "https://telegra.ph/file/3e84ce12b9b3769a728ef.jpg")
IMG_2 = getenv("IMG_2", "https://telegra.ph/file/3e84ce12b9b3769a728ef.jpg")
IMG_3 = getenv("IMG_3", "https://telegra.ph/file/3e84ce12b9b3769a728ef.jpg")
