from asyncio import sleep
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from pyrogram.errors import FloodWait
import humanize
from info import ADMINS , FLOOD, RENAMER_MODE
import random

@Client.on_message( filters.private ~ filters.forwarded & (filters.document | filters.audio | filters.video))
async def rename_start(client, message):
    if (RENAMER_MODE==True):
        if message.from_user.id in ADMINS :
            file = getattr(message, message.media.value)
            filesize = humanize.naturalsize(file.file_size) 
            filename = file.file_name
            text = f"""✏ Rename \n**Please tell, what should i do with this file.?**\n\n**File Name** :- `{filename}`\n\n<b>**File Size** </b>:- `{filesize}`"""
            buttons = [[ InlineKeyboardButton("📝 Start renaming 📝", callback_data="rename") ],
                       [ InlineKeyboardButton("❌ Close ❌", callback_data="cancel") ]]
            await message.reply_text(text=text, reply_to_message_id=message.id, reply_markup=InlineKeyboardMarkup(buttons))

        elif message.from_user.id in ADMINS :
            file = getattr(message, message.media.value)
            filesize = humanize.naturalsize(file.file_size) 
            filename = file.file_name
            try:
                text = f"""Please tell, what should i do with this file.?**\n\n**File Name** :- `{filename}`\n\n**File Size** :- `{filesize}`"""
                buttons = [[ InlineKeyboardButton("📝 Start renaming 📝", callback_data="rename") ],
                           [ InlineKeyboardButton("❌ Close ❌", callback_data="cancel") ]]
                await message.reply_text(text=text, reply_to_message_id=message.id, reply_markup=InlineKeyboardMarkup(buttons))
                await sleep(FLOOD)
            except FloodWait as e:
                await sleep(e.value)
                text = f"""Please tell, what should i do with this file.?**\n\n**File Name** :- `{filename}`\n\n**File Size** :- `{filesize}`"""
                buttons = [[ InlineKeyboardButton("📝 Start renaming 📝", callback_data="rename") ],
                           [ InlineKeyboardButton("❌ Cancel ❌", callback_data="cancel") ]]
                await message.reply_text(text=text, reply_to_message_id=message.id, reply_markup=InlineKeyboardMarkup(buttons))
            except:
                pass
        else:
            file = getattr(message, message.media.value)
            filesize = humanize.naturalsize(file.file_size) 
            filename = file.file_name
            text = f"""Please tell, what should i do with this file.?**\n\n**File Name** :- `{filename}`\n\n**File Size** :- `{filesize}`"""
            buttons = [[ InlineKeyboardButton("📝 Start renaming 📝", callback_data="rename") ],
                        [ InlineKeyboardButton("❌ Close ❌", callback_data="cancel") ]]
            await message.reply_text(text=text, reply_to_message_id=message.id, reply_markup=InlineKeyboardMarkup(buttons))
    else:
        return
