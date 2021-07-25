#(©)Codexbotz

from pyrogram import __version__
from bot import Bot
from config import OWNER_ID
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery

@Bot.on_callback_query()
async def cb_handler(client: Bot, query: CallbackQuery):
    data = query.data
    if data == "about":
        await query.message.edit_text(
            text = f"<b>○ Master : <a href='https://t.me/COLD_ONEz'>COLD_ONEz</a>\n\n○ Master : <a href='https://t.me/punisherofc'>punisher</a>\n\n○ Group : <a href='https://t.me/srsuggestionsofficial'>SR SUGGESTIONS</a>\n\n○ Channel : <a href='https://t.me/srsuggestionsmc'>SR SUGGESTIONS MC</a></b>",
            disable_web_page_preview = True,
            reply_markup = InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton("🔒 Close", callback_data = "close")
                    ]
                ]
            )
        )
    elif data == "close":
        await query.message.delete()
        try:
            await query.message.reply_to_message.delete()
        except:
            pass
