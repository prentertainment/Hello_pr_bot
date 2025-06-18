import os
from pyrogram import Client, filters

BOT_TOKEN = os.getenv("BOT_TOKEN")
API_ID = int(os.getenv("API_ID"))
API_HASH = os.getenv("API_HASH")

app = Client("my_bot", bot_token=BOT_TOKEN, api_id=API_ID, api_hash=API_HASH)

@app.on_message(filters.command("start"))
def start_handler(client, message):
    message.reply_text("Hello! Your bot is working successfully on Railway!")

app.run()