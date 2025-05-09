from pyrogram import Client, filters
from pyrogram.types import Message
import os

API_ID = 123456789 # CHANGE WITH YOUR API ID
API_HASH = "" # CHANGE WITH YOUR API HASH
BOT_TOKEN = "" # CHANGE WITH YOUR BOT TOKEN

app = Client(
    "sessions/ChatID_HyperBot",
    api_id=API_ID,
    api_hash=API_HASH,
    bot_token=BOT_TOKEN
)

@app.on_message(filters.command("start"))
async def start_command(client: Client, message: Message):
    user_id = message.from_user.id
    first_name = message.from_user.first_name
    
    await message.reply(
        f"👋 **Welcome, {first_name}!**\n\n"
        f"Your User ID: `{user_id}`\n\n"
        f"Send me any message to get your ID.\n"
        f"Forward me messages to get both your ID and the original message ID."
    )

@app.on_message(~filters.command("start"))
async def handle_all_messages(client: Client, message: Message):
    user_id = message.from_user.id
    first_name = message.from_user.first_name

    if message.forward_from or message.forward_from_chat:
        if message.forward_from:
            forward_id = message.forward_from.id
            forward_name = message.forward_from.first_name
            forward_type = "User"
            
            await message.reply(
                f"**Your User ID:** `{user_id}`\n\n"
                f"**Forwarded Message Info:**\n"
                f"• Type: {forward_type}\n"
                f"• Name: {forward_name}\n"
                f"• ID: `{forward_id}`"
            )
            
        elif message.forward_from_chat:
            forward_id = message.forward_from_chat.id
            forward_title = message.forward_from_chat.title
            
            if message.forward_from_chat.type == "channel":
                forward_type = "Channel"
            elif message.forward_from_chat.type == "supergroup":
                forward_type = "Supergroup"
            else:
                forward_type = "Group"
                
            await message.reply(
                f"**Your User ID:** `{user_id}`\n\n"
                f"**Forwarded Message Info:**\n"
                f"• Type: {forward_type}\n"
                f"• Title: {forward_title}\n"
                f"• Chat ID: `{forward_id}`"
            )
            
        else:
            await message.reply(
                f"**Your User ID:** `{user_id}`\n\n"
                f"**Forwarded Message Info:**\n"
                f"• Hidden source - Cannot retrieve ID"
            )
    else:
        await message.reply(f"**Your User ID:** `{user_id}`")

if __name__ == "__main__":
    print("Bot is starting...")
    app.run()
