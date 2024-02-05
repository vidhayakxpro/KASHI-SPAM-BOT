from telethon import __version__, events, Button

from config import X1, X2, X3, X4, X5, X6, X7, X8, X9, X10


START_BUTTON = [
    [
        Button.inline("💘 𝖢𝗈𝗆𝗆𝖺𝗇𝖽𝗌 💘", data="help_back")
    ],
    [
        Button.url("🍫 𝖣𝖾𝗏𝖾𝗅𝗈𝗉𝖾𝗋 🍫", "https://t.me/I_C2H5OH_I"),
        Button.url("🍹 𝖲𝗎𝗉𝗉𝗈𝗋𝗍 🍹", "https://t.me/FRANCIUM_OP")
    ],
    [
        Button.url("ᵛⁱᵖ°🫧𓆩𝐒ĦƖѴΔ𓆪•𝅃꯭ 🎫", "https://t.me/I_C2H5OH_I")
    ]
]


@X1.on(events.NewMessage(pattern="/start"))
@X2.on(events.NewMessage(pattern="/start"))
@X3.on(events.NewMessage(pattern="/start"))
@X4.on(events.NewMessage(pattern="/start"))
@X5.on(events.NewMessage(pattern="/start"))
@X6.on(events.NewMessage(pattern="/start"))
@X7.on(events.NewMessage(pattern="/start"))
@X7.on(events.NewMessage(pattern="/start"))
@X8.on(events.NewMessage(pattern="/start"))
@X9.on(events.NewMessage(pattern="/start"))
@X10.on(events.NewMessage(pattern="/start"))
async def start(event):              
    if event.is_private:
        AltBot = await event.client.get_me()
        bot_name = AltBot.first_name
        bot_id = AltBot.id
        TEXT = f"**ʜᴇʏ​ [{event.sender.first_name}](tg://user?id={event.sender.id}),\n\nɪ ᴀᴍ [{bot_name}](tg://user?id={bot_id})​**\n━━━━━━━━━━━━━━━━━━━\n\n"
        TEXT += f"» **𝙼𝚢 𝙳𝙴𝚅𝙴𝙻𝙾𝙿𝙴𝚁 : ᵛ ⁱ ᵖ° 🫧 𓆩𝐒 Ħ Ɩ Ѵ Δ𓆪•𝅃꯭ 🎫**\n\n"
        TEXT += f"» **𝙱𝙾𝚃𝚂 𝚅𝙴𝚁𝚂𝙸𝙾𝙽 :** `M3.3`\n"
        TEXT += f"» **𝙿𝚈𝚃𝙷𝙸𝙽 𝚅𝙴𝚁𝚂𝙸𝙾𝙽 :** `3.11.3`\n"
        TEXT += f"» **𝙵𝚁𝙰𝙽𝙲𝙸𝚄𝙼 ᴠᴇʀsɪᴏɴ :** `{__version__}`\n━━━━━━━━━━━━━━━━━"
        await event.client.send_file(
                    event.chat_id,
                    "https://telegra.ph/file/f68bff72d0fb2a6e6347f.jpg",
                    caption=TEXT, 
                    buttons=START_BUTTON
                ).
