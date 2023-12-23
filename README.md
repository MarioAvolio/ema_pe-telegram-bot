# Telegram Clown Bot

This repository contains the code for a Telegram bot that humorously modifies messages sent by a specific user in a Telegram group. When the bot detects a message from the user `@ema_pe`, it wraps the message with playful, clown-themed text.

## Features

- Listens to messages in a Telegram group.
- Identifies messages from the user `@ema_pe`.
- Modifies the message by adding a humorous prefix and suffix.
- Sends the modified message back to the group.

## Prerequisites

Before you begin, ensure you have met the following requirements:
- You have a Telegram account.
- You have created a bot on Telegram using BotFather and obtained the API token.
- You have Python installed on your machine.
- You have installed the `python-telegram-bot` library.

## Installation

To install the Telegram Clown Bot, follow these steps:

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/telegram-clown-bot.git
   ```
2. Navigate to the cloned directory:
   ```bash
   cd telegram-clown-bot
   ```
3. Install the required Python packages:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

To use the bot, you need to set your bot's API token in the script:

1. Open `bot.py` in a text editor.
2. Replace `'YOUR_TOKEN'` with your bot's API token.

To run the bot:

```bash
python bot.py
```

## Contributing to Telegram Clown Bot

To contribute to Telegram Clown Bot, follow these steps:

1. Fork this repository.
2. Create a branch: `git checkout -b <branch_name>`.
3. Make your changes and commit them: `git commit -m '<commit_message>'`.
4. Push to the original branch: `git push origin <project_name>/<location>`.
5. Create the pull request.

Alternatively, see the GitHub documentation on [creating a pull request](https://docs.github.com/en/github/collaborating-with-issues-and-pull-requests/creating-a-pull-request).

## Contributors

Thanks to the following people who have contributed to this project:

- [@yourusername](https://github.com/yourusername)

## Contact

If you want to contact me, you can reach me at `<your_email>`.

## License

This project uses the following license: [MIT License](<link_to_license>).

### Notes:
- Replace placeholders like `https://github.com/yourusername/telegram-clown-bot.git`, `@yourusername`, and `<your_email>` with your actual GitHub repository URL, username, and contact email.
- You may want to add a link to the MIT License if you choose to use it.
- This README assumes that the main script of your bot is named `bot.py`. Adjust the filename in the instructions if it's different.
- The 'Contributing' section is generic. You can customize it based on how you want contributors to participate in your project.
