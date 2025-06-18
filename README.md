# 🤖 Telegram Bot Using Pyrogram - Deploy Ready for Railway

This is a simple starter Telegram bot built using **Pyrogram**, designed to help you easily deploy your bot on platforms like **Railway** or **Render**.

---

## 📌 Features

- Responds to `/start` command with a welcome message
- Simple and lightweight template
- Easily extendable with Pyrogram features
- Ready-to-deploy configuration for Railway

---

## 📁 Project Structure

---

## 🔐 Environment Variables

You need to set the following environment variables (in `.env` or in Railway dashboard):

| Variable     | Description |
|--------------|-------------|
| `BOT_TOKEN`  | Get it from [@BotFather](https://t.me/BotFather) |
| `API_ID`     | Get it from [my.telegram.org](https://my.telegram.org) |
| `API_HASH`   | Same as above |

---

## 🚀 Deploy on Railway

1. Fork or upload this repo to your GitHub account.
2. Go to [Railway](https://railway.app/).
3. Create a new project → Deploy from GitHub.
4. Add the required environment variables (`BOT_TOKEN`, `API_ID`, `API_HASH`).
5. Set the **Start Command** (if not auto-detected):
6. Done! Your bot is now live ✅

---

## 🧠 How to Extend

You can extend this bot to:
- Add AutoFilter using MongoDB
- Add inline buttons
- Add file-sharing or channel management features
- Respond to custom commands or messages

---

## 👤 Credits

Created with ❤️ by [Drama Tv24](https://t.me/DramaTv24)

---

## 📢 License

This project is licensed under the MIT License - feel free to use and modify.
