from pyrogram.types import InlineKeyboardMarkup
from button import styled_button, ButtonStyle

# --- Buttons logic for the music player ---

def close_markup():
    """Ye keyboard tab use karna jab player band ho ya normal info dena ho."""
    return InlineKeyboardMarkup(
        [
            [
                styled_button(text="『 ♡ 𝐀ᴅᴅ 𝐌є 𝐁ᴀʙʏ ♡ 』", url="https://t.me/Sizzumusicbot?startgroup=true", style=ButtonStyle.SUCCESS),
                styled_button(text="✯ CLOSE ✯", callback_data="close", style=ButtonStyle.DANGER)
            ]
        ]
    )

def stream_markup(chat_id):
    """Ye main player keyboard hai jo music ke time dikhega."""
    return InlineKeyboardMarkup(
        [
            # Row 1: Playback Controls
            [
                styled_button(text="▷", callback_data=f"ADMIN Resume|{chat_id}", style=ButtonStyle.SUCCESS),
                styled_button(text="II", callback_data=f"ADMIN Pause|{chat_id}", style=ButtonStyle.DANGER),
                styled_button(text="‣‣I", callback_data=f"ADMIN Skip|{chat_id}", style=ButtonStyle.PRIMARY),
                styled_button(text="▢", callback_data=f"ADMIN Stop|{chat_id}", style=ButtonStyle.DANGER),
            ],
            # Row 2: Seeking Controls
            [
                styled_button(text="⏪ 20s", callback_data=f"ADMIN SeekBack|{chat_id}", style=ButtonStyle.PRIMARY),
                styled_button(text="20s ⏩", callback_data=f"ADMIN SeekForward|{chat_id}", style=ButtonStyle.PRIMARY),
            ],
            # Row 3: Branding & Closing
            [
                styled_button(text="『 ✦ 𝐂ʟᴏηє 𝐌є ✦ 』", url="https://t.me/SizzuMusicBot", style=ButtonStyle.SUCCESS),
                styled_button(text="✯ CLOSE ✯", callback_data="close", style=ButtonStyle.DANGER)
            ]
        ]
    )

# --- Example Usage ---
# Jab tujhe message bhejna ho:
# await message.reply_photo(
#     photo="link_ya_file_id",
#     caption="Playing Music...",
#     reply_markup=stream_markup(message.chat.id)
# )
