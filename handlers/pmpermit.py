from callsmusic.callsmusic import client as USER
from pyrogram import filters
from pyrogram.types import Chat, Message, User, InlineKeyboardMarkup, InlineKeyboardButton


@USER.on_message(filters.text & filters.private & ~filters.me & ~filters.bot)
async def pmPermit(client: USER, message: Message):
  await USER.send_message(message.chat.id,"Hi there, This is a kaori's assistant userbot service .\n\n Info:\n - Only work with specified groups.\n - if you wanna use me  contact owner @WalkersChatt and ping ```@MizuharaChizru```.\n\n❗️ Rules:\n   - No chatting allowed\n   - No spam allowed \n\n 👉 **SEND GROUP INVITE LINK OR USERNAME IF USERBOT CAN'T JOIN YOUR GROUP.**\n\n ⚠️ Disclamer: If you are sending a message here it means admin will see your message and join chat.\n\n")
  return                        
@USER.on_message(filters.sticker & filters.private & ~filters.me & ~filters.bot)
async def pmPermit(client: USER, message: Message):
  await USER.send_message(message.chat.id,"Hi there, This is a kaori's assistant userbot service .\n\n Info:\n - Only work with specified groups.\n - if you wanna use me  contact owner @WalkersChatt and ping ```@MizuharaChizru```.\n\n❗️ Rules:\n   - No chatting allowed\n   - No spam allowed \n\n 👉 **SEND GROUP INVITE LINK OR USERNAME IF USERBOT CAN'T JOIN YOUR GROUP.**\n\n ⚠️ Disclamer: If you are sending a message here it means admin will see your message and join chat.\n\n"
  reply_markup=InlineKeyboardMarkup(
              [[
              InlineKeyboardButton(text="🎙️ Support Group 🎙️", url="https://t.me/WalkersChatt")
              ]]
          ))
  return                        