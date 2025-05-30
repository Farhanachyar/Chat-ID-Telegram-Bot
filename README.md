# 🤖 Telegram Chat ID Bot


<p align="center">
  <h4 align="center">A simple Telegram bot that helps users find their User ID and the Chat ID of forwarded messages.</h4>

  <p align="center">
    <a href="https://codeclimate.com/github/Farhanachyar/Chat-ID-Telegram-Bot/maintainability"><img src="https://api.codeclimate.com/v1/badges/c60f42d7d0b61bd33e98/maintainability" /></a>
    <a href="https://github.com/Farhanachyar/Chat-ID-Telegram-Bot/actions/workflows/test-deploy.yml"><img src="https://github.com/Farhanachyar/Chat-ID-Telegram-Bot/actions/workflows/test-deploy.yml/badge.svg" /></a>
    <a href="https://github.com/Farhanachyar/Chat-ID-Telegram-Bot/issues"><img src="https://img.shields.io/github/issues/Farhanachyar/Chat-ID-Telegram-Bot"/></a>
    <a href="https://github.com/Farhanachyar/Chat-ID-Telegram-Bot/stargazers"><img src="https://img.shields.io/github/stars/Farhanachyar/Chat-ID-Telegram-Bot"/></a>
    <a href="https://github.com/Farhanachyar/Chat-ID-Telegram-Bot/network/members"><img src="https://img.shields.io/github/forks/Farhanachyar/Chat-ID-Telegram-Bot"/></a>
    <a href="https://github.com/Farhanachyar/Chat-ID-Telegram-Bot/commits/main"><img src="https://img.shields.io/github/last-commit/Farhanachyar/Chat-ID-Telegram-Bot/main"/></a>
    <a href="https://github.com/arifszn/gitprofile/blob/main/CONTRIBUTING.md"><img src="https://img.shields.io/badge/contributions-welcome-brightgreen.svg?style=flat"/></a>
    <a href="https://github.com/Farhanachyar/Chat-ID-Telegram-Bot/blob/main/LICENSE"><img src="https://img.shields.io/github/license/Farhanachyar/Chat-ID-Telegram-Bot"/></a>

  </p>

  <p align="center">
    <a href="https://github.com/Farhanachyar/Chat-ID-Telegram-Bot/issues">Report Bug</a>
    ·
    <a href="https://github.com/Farhanachyar/Chat-ID-Telegram-Bot/discussions">Request Feature</a>
  </p>
</p>

## ✨ Features

- 🆔 Get your Telegram User ID instantly
- 📨 Retrieve Chat ID from forwarded messages (channels, groups, users)
- 🔄 Simple and clean responses
- 🌐 Ready for deployment on Koyeb

## 📋 Prerequisites

- Python 3.6 or higher
- Pyrogram library
- A Telegram account
- Bot token from [@BotFather](https://t.me/BotFather)

## 🚀 Installation

### Step 1: Clone the repository

```bash
git clone https://github.com/yourusername/telegram-chat-id-bot.git
cd telegram-chat-id-bot
```

### Step 2: Install dependencies

```bash
pip install -r requirements.txt
```

### Step 3: Get your API credentials

1. **API ID & API Hash**:
   - Visit [my.telegram.org](https://my.telegram.org/auth)
   - Log in with your phone number
   - Click on "API Development tools"
   - Create a new application (fill in all required fields)
   - Your API ID and Hash will be displayed

2. **Bot Token**:
   - Start a chat with [@BotFather](https://t.me/BotFather) on Telegram
   - Send `/newbot` and follow the instructions
   - Choose a name and username for your bot
   - Once created, you'll receive a bot token
   - Copy this token for the next step

### Step 4: Configure the bot

Edit `main.py` and replace the placeholder values with your actual credentials:

```python
API_ID = your_api_id  # Replace with your API ID (integer)
API_HASH = "your_api_hash"  # Replace with your API Hash
BOT_TOKEN = "your_bot_token"  # Replace with your Bot Token
```

### Step 5: Run the bot

```bash
python main.py
```

## 🐳 Docker Deployment

This repository includes a Dockerfile for easy deployment.

```bash
# Build the Docker image
docker build -t telegram-chat-id-bot .

# Run the container
docker run -d telegram-chat-id-bot
```

## ☁️ Koyeb Deployment

1. Fork this repository
2. Create a new Koyeb account if you don't have one
3. Connect your GitHub account to Koyeb
4. Create a new service from your forked repo
5. The included Dockerfile and health check will handle the setup automatically

## 📝 Usage

1. Start a chat with your bot on Telegram
2. Send `/start` to begin
3. Send any message to get your User ID
4. Forward a message from any chat to get its Chat ID

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 🤝 Contributing

Contributions are welcome! Feel free to open an issue or submit a pull request.

## ⭐ Support

If you find this project helpful, please consider giving it a star on GitHub! It helps a lot.

<a href="https://github.com/Farhanachyar/Chat-ID-Telegram-Bot/stargazers"><img src="https://img.shields.io/github/stars/farhanachyar/Chat-ID-Telegram-Bot"/></a>

You can also:
- 💻 Check out my other projects on [GitHub](https://github.com/farhanachyar)


Your support motivates me to create more useful tools and projects!

---

Made with ❤️ by [Farhanachyar]
