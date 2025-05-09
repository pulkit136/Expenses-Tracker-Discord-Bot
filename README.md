# 💸 Expenses Tracker Discord Bot

A simple Discord bot to help you track your daily expenses seamlessly. Log your expenses directly through Discord messages, and the bot will record them for easy tracking and analysis.

---

## 🚀 Features

- **Quick Expense Logging**: Add expenses by sending messages in the format `amount, item` or `amount, item, place`.
- **Daily Summary**: Retrieve a summary of today's expenses.
- **Total Expenditure**: Get the total amount spent over time.
- **User-Friendly Commands**: Simple commands to interact with the bot.

---

## 🛠️ Setup Instructions

### Prerequisites

- Python 3.6 or higher
- A Discord account
- A Discord bot token

### Installation

1. **Clone the Repository**

   ```bash
   git clone https://github.com/pulkit136/Expenses-Tracker-Discord-Bot.git
   cd Expenses-Tracker-Discord-Bot
   
2. **Install Dependencies**
   `pip install -r requirements.txt`

3. Set Up Environment Variables
   Create a .env file in the root directory and add the following:
   `DISCORD_TOKEN=your_discord_bot_token_here`
   
5. Run the Bot
   `python bot.py`


## 📖 Usage
Once the bot is running and added to your Discord server:

### Logging an Expense
Send a message to the bot in either of the following formats:

`amount, item`
`amount, item, place`

### Examples 
`150, Lunch`
`45, Samosa, Bikaner`

### Commands
`!total` — Displays the total expenses recorded.

`!today` — Shows today's expenses.

`!help` — Lists available commands and usage instructions.

## File structure 
Expenses-Tracker-Discord-Bot/
│
├── bot.py               # Main bot script
├── requirements.txt     # Dependencies
└── .env                 # (To be created) Environment file for your bot token

## 🤝 Contributing
Contributions are welcome! If you find a bug or want to add a feature:

- Fork the repo

- Create a new branch (git checkout -b feature-xyz)

- Commit your changes (git commit -m 'Add feature xyz')

- Push to the branch (git push origin feature-xyz)

- Open a pull request
