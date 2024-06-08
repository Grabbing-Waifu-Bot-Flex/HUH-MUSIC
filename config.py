import os
import re
from os import getenv

from dotenv import load_dotenv
from pyrogram import filters

load_dotenv()
# Get this value from my.telegram.org/apps
API_ID = int(getenv("API_ID", "20533795"))
API_HASH = getenv("API_HASH", "f6cadf28523943f525e706e6ace8a250")

# Get your token from @BotFather on Telegram.
BOT_TOKEN = getenv("BOT_TOKEN", "7405146014:AAF5Wie0qJWA53zxW_1kBJ6nNzMw9Va5Q6Y")

# Get your mongo url from cloud.mongodb.com
MONGO_DB_URI = getenv("MONGO_DB_URI", "mongodb+srv://Zxcdc:zxchypernjqjjqv8762@cluster0.hcgtozy.mongodb.net/?retryWrites=true&w=majority")

DURATION_LIMIT_MIN = int(getenv("DURATION_LIMIT", 999999999))

# Chat id of a group for logging bot's activities
LOGGER_ID = int(getenv("LOGGER_ID", "-1002078575375"))
LOG_GROUP_ID = int(getenv("LOG_GROUP_ID", "-1002078575375"))

# Get this value from  on Telegram by /id
OWNER_ID = int(getenv("OWNER_ID", "6584789596"))

# Fill these variables if you're deploying on heroku.
# Your heroku app name
HEROKU_APP_NAME = getenv("flex-music-x-opx")
# Get it from http://dashboard.heroku.com/account
HEROKU_API_KEY = getenv("HRKU-f768e60f-b57f-4587-81f1-110a599578fa)

UPSTREAM_REPO = getenv(
    "UPSTREAM_REPO",
    "https://github.com/THE-VIP-BOY-OP/VIP-MUSIC",
)
UPSTREAM_BRANCH = getenv("UPSTREAM_BRANCH", "master")
GIT_TOKEN = getenv(
    "GIT_TOKEN", None
)  # Fill this variable if your upstream repository is private

SUPPORT_CHANNEL = getenv("SUPPORT_CHANNEL", "https://t.me/FleX_Bots_News")
SUPPORT_CHAT = getenv("SUPPORT_CHAT", "https://t.me/Flex_Support_Chat")

# Maximum Limit Allowed for users to save playlists on bot's server
SERVER_PLAYLIST_LIMIT = int(getenv("SERVER_PLAYLIST_LIMIT", "100"))

RADIO_URL = getenv("RADIO_URL", "http://peridot.streamguys.com:7150/Mirchi")

# Don't fill here any YouTube link fill here any direct acessable audio link

# MaximuM limit for fetching playlist's track from youtube, spotify, apple
# links.
PLAYLIST_FETCH_LIMIT = int(getenv("PLAYLIST_FETCH_LIMIT", "100"))
# Set this to True if you want the assistant to automatically leave chats
# after an interval
AUTO_LEAVING_ASSISTANT = False

# Auto Gcast/Broadcast Handler, Write:- [On / Off] During Hosting, Dont Do
# anything here.)
AUTO_GCAST = os.getenv("AUTO_GCAST")

# Auto Broadcast Message That You Want Use In Auto Broadcast In All Groups.
AUTO_GCAST_MSG = getenv("AUTO_GCAST_MSG", "")

# Get this credentials from https://developer.spotify.com/dashboard
SPOTIFY_CLIENT_ID = getenv("SPOTIFY_CLIENT_ID", "19609edb1b9f4ed7be0c8c1342039362")
SPOTIFY_CLIENT_SECRET = getenv(
    "SPOTIFY_CLIENT_SECRET", "409e31d3ddd64af08cfcc3b0f064fcbe"
)


# Maximum limit for fetching playlist's track from youtube, spotify, apple
# links.
PLAYLIST_FETCH_LIMIT = int(getenv("PLAYLIST_FETCH_LIMIT", 2500))


# Telegram audio and video file size limit (in bytes)
TG_AUDIO_FILESIZE_LIMIT = int(getenv("TG_AUDIO_FILESIZE_LIMIT", 104857600))
TG_VIDEO_FILESIZE_LIMIT = int(getenv("TG_VIDEO_FILESIZE_LIMIT", 1073741824))
# Checkout https://www.gbmb.org/mb-to-bytes for converting mb to bytes

# Time after which bot will suggest random chats about bot commands.
AUTO_SUGGESTION_TIME = int(
    getenv("AUTO_SUGGESTION_TIME", "3")
)  # Remember to give value in Seconds

# Set it True if you want to bot to suggest about bot commands to random
# chats of your bots.
AUTO_SUGGESTION_MODE = getenv("AUTO_SUGGESTION_MODE", "True")
# Cleanmode time after which bot will delete its old messages from chats
CLEANMODE_DELETE_MINS = int(
    getenv("CLEANMODE_MINS", "5")
)  # Remember to give value in Seconds

# Get your pyrogram v2 session from @VIP_STRING_ROBOT on Telegram
STRING1 = getenv("STRING_SESSION", "BQE5UiMAWc29BV3LHGXnRCirf5kABbHLJoyhHCieRlVKXcsP-kyRoZnItKUpnFBhsMYqJ-Dv-hOMEpWFTuNlD4vTqTEsIFfXdIvaB84i5ERJfG3GgarTut9iRx5Za21wK5WPW-U7JtNQ2jpOeHNJtoxKkZdynk9CBh58SGMg-pUwyr4s2P6YnUn2UCe3iG_ZslQ2uEyMZJ6LGszXb1qg7zm2f9eSWaj9ndyJ-03SyXpG0WjVFB_Tb5tjQlpyIhcuT9hgJCsfdqcKTw5Wr7YcLvlaV-GQKNPff8CmjctXvWMTXu_b80FWE8bpHao3z4sHiVi2iFT9QLQ0Kkbf92H_3JSd3osdUwAAAAF-Ni2lAA")
STRING2 = getenv("STRING_SESSION2", None)
STRING3 = getenv("STRING_SESSION3", None)
STRING4 = getenv("STRING_SESSION4", None)
STRING5 = getenv("STRING_SESSION5", None)


#    __      _______ _____    ___  __ _    _  _____ _____ _____   _____
#    \ \    / /_   _|  __ \   |  \/  | |  | |/ ____|_   _/ ____|  |  _ \ / __ \__   __|
#     \ \  / /  | | | |__) |  | \  / | |  | | (___   | || |       | |_) | |  | | | |
#      \ \/ /   | | |  ___/   | |\/| | |  | |\___ \  | || |       |  _ <| |  | | | |
#       \  /   _| |_| |       | |  | | |__| |____) |_| || |____   | |_) | |__| | | |
#        \/   |_____|_|       |_|  |_|\____/|_____/|_____\_____|  |____/ \____/  |_|


BANNED_USERS = filters.user()
adminlist = {}
lyrical = {}
votemode = {}
autoclean = []
confirmer = {}
chatstats = {}
userstats = {}
clean = {}

autoclean = []

START_IMG_URL = getenv(
    "START_IMG_URL", "https://te.legra.ph/file/ecdeac045f4045c198bd6.jpg"
)
PING_IMG_URL = getenv(
    "PING_IMG_URL", "https://te.legra.ph/file/ecdeac045f4045c198bd6.jpg"
)
PLAYLIST_IMG_URL = "https://te.legra.ph/file/ecdeac045f4045c198bd6.jpg"
STATS_IMG_URL = "https://te.legra.ph/file/ecdeac045f4045c198bd6.jpg"
TELEGRAM_AUDIO_URL = "https://te.legra.ph/file/ecdeac045f4045c198bd6.jpg"
TELEGRAM_VIDEO_URL = "https://te.legra.ph/file/ecdeac045f4045c198bd6.jpg"
STREAM_IMG_URL = "https://te.legra.ph/file/ecdeac045f4045c198bd6.jpg"
SOUNCLOUD_IMG_URL = "https://te.legra.ph/file/ecdeac045f4045c198bd6.jpg"
YOUTUBE_IMG_URL = "https://te.legra.ph/file/ecdeac045f4045c198bd6.jpg"
SPOTIFY_ARTIST_IMG_URL = "https://te.legra.ph/file/ecdeac045f4045c198bd6.jpg"
SPOTIFY_ALBUM_IMG_URL = "https://te.legra.ph/file/ecdeac045f4045c198bd6.jpg"
SPOTIFY_PLAYLIST_IMG_URL = "https://te.legra.ph/file/ecdeac045f4045c198bd6.jpg"


def time_to_seconds(time):
    stringt = str(time)
    return sum(int(x) * 60**i for i, x in enumerate(reversed(stringt.split(":"))))


DURATION_LIMIT = int(time_to_seconds(f"{DURATION_LIMIT_MIN}:00"))


if SUPPORT_CHANNEL:
    if not re.match("(?:http|https)://", SUPPORT_CHANNEL):
        raise SystemExit(
            "[ERROR] - Your SUPPORT_CHANNEL url is wrong. Please ensure that it starts with https://"
        )

if SUPPORT_CHAT:
    if not re.match("(?:http|https)://", SUPPORT_CHAT):
        raise SystemExit(
            "[ERROR] - Your SUPPORT_CHAT url is wrong. Please ensure that it starts with https://"
        )
