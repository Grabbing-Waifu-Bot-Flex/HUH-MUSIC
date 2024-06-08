from pyrogram.types import InlineKeyboardButton

import config
from VIPMUSIC import app


def start_panel(_):
    buttons = [
        [
            InlineKeyboardButton(
                text=_["S_B_1"], url=f"https://t.me/{app.username}?startgroup=true"
            ),
        ],
        [
            InlineKeyboardButton(text="Hᴇʟᴘ", callback_data="settings_back_helper"),
            InlineKeyboardButton(text="Sᴇᴛ", callback_data="settings_helper"),
        ],
        [
            InlineKeyboardButton(text="Gʀᴏᴜᴘ", url=config.SUPPORT_CHAT),
        ],
    ]
    return buttons


def private_panel(_):
    buttons = [
        [
            InlineKeyboardButton(
                text="ᴀᴅᴅ ᴍᴇ ɪɴ ɴᴇᴡ ɢʀᴏᴜᴘs",
                url=f"https://t.me/{app.username}?startgroup=true",
            )
        ],
        [
            InlineKeyboardButton(text="Gʀᴏᴜᴘ", url=config.SUPPORT_CHAT),
            InlineKeyboardButton(text="ᴍᴏʀᴇ", url=config.SUPPORT_CHANNEL),
        ],
        [
            InlineKeyboardButton(
                text="ғᴇᴀᴛᴜʀᴇs", callback_data="settings_back_helper"
            )
        ],
    ]
    return buttons
