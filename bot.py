import os
import threading
from http.server import BaseHTTPRequestHandler, HTTPServer
from pyrogram import Client, filters
print("✅ Code loaded, before importing Pyrogram")
from pyrogram import Client
print("✅ Imported Pyrogram")

#... বাকি কোড
BOT_TOKEN = os.getenv("BOT_TOKEN")
API_ID = int(os.getenv("API_ID", 0))
API_HASH = os.getenv("API_HASH")

app = Client("my_bot", bot_token=BOT_TOKEN, api_id=API_ID, api_hash=API_HASH)

# Health check server setup
class HealthHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/plain')
        self.end_headers()
        self.wfile.write(b'OK')

def run_health_server():
    port = int(os.getenv("PORT", 8000))
    server = HTTPServer(('', port), HealthHandler)
    print(f"Health server running on port {port}")
    server.serve_forever()

# Bot command handlers
@app.on_message(filters.command("start"))
def start_handler(client, message):
    message.reply_text("Hello! Your bot is working successfully on Railway!")

if __name__ == "__main__":
    # Start health server in a separate thread
    health_thread = threading.Thread(target=run_health_server, daemon=True)
    health_thread.start()
    
    # Start the Telegram bot
    print("SHello! Your bot is working successfully on Railway! ")
    app.run()
