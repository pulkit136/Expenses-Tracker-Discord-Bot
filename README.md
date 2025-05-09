💸 Expenses Tracker Discord Bot
A simple Discord bot to help you track your daily expenses seamlessly. Log your expenses directly through Discord messages, and the bot will record them for easy tracking and analysis.

🚀 Features
Quick Expense Logging: Add expenses by sending messages in the format amount, item or amount, item, place.

Daily Summary: Retrieve a summary of today's expenses.

Total Expenditure: Get the total amount spent over time.

User-Friendly Commands: Simple commands to interact with the bot.

🛠️ Setup Instructions
Prerequisites
Python 3.6 or higher

A Discord account

A Discord bot token

Installation
Clone the Repository

bash
Copy
Edit
git clone https://github.com/pulkit136/Expenses-Tracker-Discord-Bot.git
cd Expenses-Tracker-Discord-Bot
Install Dependencies

Ensure you have pip installed. Then, run:

bash
Copy
Edit
pip install -r requirements.txt
Configure Environment Variables

Create a .env file in the root directory and add your Discord bot token:

env
Copy
Edit
DISCORD_TOKEN=your_discord_bot_token_here
Run the Bot

bash
Copy
Edit
python bot.py
📖 Usage
Once the bot is running and added to your Discord server:

Log an Expense

Send a direct message to the bot in the following format:

Copy
Edit
amount, item
or

Copy
Edit
amount, item, place
Example:

Copy
Edit
150, Lunch
45, Samosa, Bikaner
Commands

!total: Displays the total expenses recorded.

!today: Shows today's expenses.

!help: Provides information on how to use the bot.

📁 File Structure
bot.py: Main bot script containing the logic for handling messages and commands.

requirements.txt: Lists the Python dependencies required to run the bot.

🤝 Contributing
Contributions are welcome! Please fork the repository and submit a pull request for any enhancements or bug fixes.
