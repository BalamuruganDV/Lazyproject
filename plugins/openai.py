from utils import temp
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from pyrogram import Client, filters
from info import *
import openai
openai.api_key = OPENAI_API

@Client.on_message(filters.command("ask"))
async def lazy_answer(client, message):
    if AI == True: 
        user_id = message.from_user.id
        if user_id:
            try:
                lazy_users_message = message.text
                user_id = message.from_user.id
                response = openai.Completion.create(
                    model = "text-davinci-003",
                    prompt = lazy_users_message,
                    temperature = 0.5, 
                    max_tokens = 1000,
                    top_p=1,
                    frequency_penalty=0.1,
                    presence_penalty = 0.0,
                )
                btn=[
                        [InlineKeyboardButton(text=f"⇱🤷‍♀️ Take Action 🗃️⇲", url=f'https://t.me/{temp.U_NAME}')],
                        [InlineKeyboardButton(text=f"🗑 Delete log ❌", callback_data=f'close_data')],
                    ]
                reply_markup=InlineKeyboardMarkup(btn)
                lazy_response = response.choices[0].text 
                await client.send_message(AI_LOGS, text=f"⚡️⚡️#AI_Query \n<b> User </b> :- {message.from_user.mention}\n<b> User id </b> :- {user_id}\n\n<b> Asked me </b> \n {lazy_users_message} \n\n<b> I responded </b>{lazy_response}", 
                reply_markup = reply_markup )
                await message.reply(f"{lazy_response}")
            except Exception as error:
                print(error)
                await message.reply_text(f'Error occured\n\n{error}')
    else:
        return
