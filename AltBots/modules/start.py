from telethon import __version__, events, Button
from telethon.tl.custom import Button.inline
from telethon.tl.types import InlineKeyboardMarkup, InlineKeyboardButton

from config import X1, X2, X3, X4, X5, X6, X7, X8, X9, X10

START_BUTTON = InlineKeyboardMarkup(
    [
        [InlineKeyboardButton.text("💘 𝙲𝚘𝚖𝚖𝚊𝚗𝚍𝚂 💘", callback_data="help_back")],
        [
            InlineKeyboardButton.url("🌺 𝙳𝚎𝚟𝚎𝚕𝚘𝚙𝚎𝚁 🌺", "https://t.me/PRADHAN474"),
            InlineKeyboardButton.url("🌸 𝚂𝚞𝚙𝚙𝚘𝚛𝚃 🌸", "https://t.me/BWANDARLOK"),
        ],
        [InlineKeyboardButton.url("💖 𝙾𝚡𝚢𝙶𝚎𝙽 💖", "https://t.me/PRADHAN474")],
    ]
)

async def start(event):
    if event.is_private:
        alt_bot = await event.client.get_me()
        bot_name = alt_bot.first_name
        bot_id = alt_bot.id

        text = (
            f"**ʜᴇʏ​ [{event.sender.first_name}](tg://user?id={event.sender.id}),\n\n"
            f"ɪ ᴀᴍ [{bot_name}](tg://user?id={bot_id})​**\n━━━━━━━━━━━━━━━━━━━\n\n"
            f"» **𝙼𝚢 𝙳𝙴𝚅𝙴𝙻𝙾𝙿𝙴𝚁 : 🦋⃟ ᴠͥɪͣᴘͫ 🇴 🇽 𝐘 𝐆 𝐄 𝐍⃝⃝⃪⃕🥀**\n\n"
            f"» **𝙱𝙾𝚃𝚂 𝚅𝙴𝚁𝚂𝙸𝙾𝙽 :** `M3.3`\n"
            f"» **𝙿𝚈𝚃𝙷𝙸𝙽 𝚅𝙴𝚁𝚂𝙸𝙾𝙽 :** `3.11.3`\n"
            f"» **𝙾𝚇𝚈𝙶𝙴𝙽 ᴠᴇʀsɪᴏɴ :** `{__version__}`\n━━━━━━━━━━━━━━━━━"
        )

        await event.client.send_file(
            event.chat_id,
            "https://graph.org/file/b0825ba6490d2aa6a6afd.jpg",
            caption=text,
            buttons=START_BUTTON,
        )
