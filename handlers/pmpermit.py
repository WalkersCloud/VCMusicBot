from callsmusic.callsmusic import client as USER
from pyrogram import filters
from pyrogram.types import Chat, Message, User


@USER.on_message(filters.text & filters.private & ~filters.me & ~filters.bot)
async def pmPermit(client: USER, message: Message):
  await USER.send_message(message.chat.id,"Hola👋! , This is Kaori's assistant userbot service .\n\n ❗️ **Rules:**\n   - No chatting allowed\n   - No spam allowed \n\nℹ️ **Info:** \n - You can't add this user to  your group \n - If you want to add contact owner @WalkersChatt and ping ```@MizuharaChizru```\n\n ⚠️ Disclamer: If you are sending a message here it means admin will see your message and join chat\n   - Don't add this user to secret groups. \n   - Don't Share private info here\n\n" )
  return                        
@USER.on_message(filters.sticker & filters.private & ~filters.me & ~filters.bot)
async def pmPermit(client: USER, message: Message):
  await USER.send_message(
    chat_id=message.chat.id,
    text="hello",
    reply_to_message_id=message.message_id
    )
  return                        