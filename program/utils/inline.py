""" inline section button """

from pyrogram.types import (
  InlineKeyboardButton,
  InlineKeyboardMarkup,
)


def stream_markup(user_id):
  buttons = [
        [
            InlineKeyboardButton("II", callback_data=f'set_pause | {user_id}'),
            InlineKeyboardButton("▷", callback_data=f'set_resume | {user_id}'),
            InlineKeyboardButton("‣‣I", callback_data=f'set_skip | {user_id}'),
            InlineKeyboardButton("▢", callback_data=f'set_stop | {user_id}'),
        ],
        [
            InlineKeyboardButton("𓆩👑❛ Azam ♕︎ 𝐖𝐨𝐫𝐥𝐝᭄ ❜👑𓆪", url=f"https://t.me/azam_sharif_gorup")
        ]
    ]
  return buttons


def menu_markup(user_id):
  buttons = [
    [
      InlineKeyboardButton(text="⏹", callback_data=f'set_stop | {user_id}'),
      InlineKeyboardButton(text="⏸", callback_data=f'set_pause | {user_id}'),
      InlineKeyboardButton(text="▶️", callback_data=f'set_resume | {user_id}'),
    ],
    [
      InlineKeyboardButton(text="🔇", callback_data=f'set_mute | {user_id}'),
      InlineKeyboardButton(text="🔊", callback_data=f'set_unmute | {user_id}'),
    ],
    [
      InlineKeyboardButton(text="🔙 Go Back", callback_data='stream_home_panel'),
    ]
  ]
  return buttons


close_mark = InlineKeyboardMarkup(
  [
    [
      InlineKeyboardButton(
        "🗑 Close", callback_data="set_close"
      )
    ]
  ]
)


back_mark = InlineKeyboardMarkup(
  [
    [
      InlineKeyboardButton(
        "🔙 Go Back", callback_data="stream_menu_panel"
      )
    ]
  ]
)
