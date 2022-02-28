""" inline section button """

from pyrogram.types import (
  CallbackQuery,
  InlineKeyboardButton,
  InlineKeyboardMarkup,
  Message,
)


def stream_markup(user_id):
  buttons = InlineKeyboardMarkup(
    [
        [
            InlineKeyboardButton("II", callback_data="pause"),
            InlineKeyboardButton("▷", callback_data="resume"),
            InlineKeyboardButton("‣‣I", callback_data="skip"),
            InlineKeyboardButton("▢", callback_data="end"),
        ],
        [
            InlineKeyboardButton("𓆩👑❛ 𝐋𝐮𝐜𝐤𝐲 ♕︎ 𝐖𝐨𝐫𝐥𝐝᭄ ❜👑𓆪", url=f"https://t.me/terayaarhoomai")
        ]
    ]
)
  return buttons


def menu_markup(user_id):
  buttons = [
    [
      InlineKeyboardButton(text="⏹", callback_data=f'cbstop | {user_id}'),
      InlineKeyboardButton(text="⏸", callback_data=f'cbpause | {user_id}'),
      InlineKeyboardButton(text="▶️", callback_data=f'cbresume | {user_id}'),
    ],
    [
      InlineKeyboardButton(text="🔇", callback_data=f'cbmute | {user_id}'),
      InlineKeyboardButton(text="🔊", callback_data=f'cbunmute | {user_id}'),
    ],
    [
      InlineKeyboardButton(text="🗑 Close", callback_data='cls'),
    ]
  ]
  return buttons


close_mark = InlineKeyboardMarkup(
  [
    [
      InlineKeyboardButton(
        "🗑 Close", callback_data="cls"
      )
    ]
  ]
)


back_mark = InlineKeyboardMarkup(
  [
    [
      InlineKeyboardButton(
        "🔙 Go Back", callback_data="cbmenu"
      )
    ]
  ]
)
