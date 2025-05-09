# 🤖 Telegram Chat ID Bot

A simple Telegram bot that helps users find their User ID and the Chat ID of forwarded messages.

<p align="center">
  <img src="https://user-images.githubusercontent.com/45073703/177566625-9b84e793-4559-4475-ba54-8d3d5f4123d4.png" width="35%">

  <h4 align="center">Easy to use automatic portfolio builder for every GitHub user!</h4>

  <p align="center">
    <a href="https://codeclimate.com/github/arifszn/gitprofile/maintainability"><img src="https://api.codeclimate.com/v1/badges/c60f42d7d0b61bd33e98/maintainability" /></a>
    <a href="https://github.com/arifszn/gitprofile/actions/workflows/test-deploy.yml"><img src="https://github.com/arifszn/gitprofile/actions/workflows/test-deploy.yml/badge.svg" /></a>
    <a href="https://github.com/arifszn/gitprofile/issues"><img src="https://img.shields.io/github/issues/arifszn/gitprofile"/></a>
    <a href="https://github.com/arifszn/gitprofile/stargazers"><img src="https://img.shields.io/github/stars/arifszn/gitprofile"/></a>
    <a href="https://github.com/arifszn/gitprofile/network/members"><img src="https://img.shields.io/github/forks/arifszn/gitprofile"/></a>
    <a href="https://github.com/arifszn/gitprofile/commits/main"><img src="https://img.shields.io/github/last-commit/arifszn/gitprofile/main"/></a>
    <a href="https://github.com/arifszn/gitprofile/blob/main/CONTRIBUTING.md"><img src="https://img.shields.io/badge/contributions-welcome-brightgreen.svg?style=flat"/></a>
    <a href="https://github.com/arifszn/gitprofile/blob/main/LICENSE"><img src="https://img.shields.io/github/license/arifszn/gitprofile"/></a>
    <a href="https://idx.google.com/import?url=https%3A%2F%2Fgithub.com%2Farifszn%2Fgitprofile"><picture>
        <source media="(prefers-color-scheme: dark)" srcset="https://cdn.idx.dev/btn/open_dark_20.svg">
        <source media="(prefers-color-scheme: light)" srcset="https://cdn.idx.dev/btn/open_light_20.svg">
        <img height="20" alt="Open in IDX" src="https://cdn.idx.dev/btn/open_purple_20.svg">
      </picture></a>
  </p>

  <p align="center">
    <a href="https://arifszn.github.io/gitprofile">View Demo</a>
    ·
    <a href="https://github.com/arifszn/gitprofile/issues">Report Bug</a>
    ·
    <a href="https://github.com/arifszn/gitprofile/discussions">Request Feature</a>
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
