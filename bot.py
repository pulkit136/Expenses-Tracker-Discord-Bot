import os
import re
from datetime import datetime

import discord
from discord.ext import commands
import gspread
from google.oauth2.service_account import Credentials
from dotenv import load_dotenv

# Load environment variables
load_dotenv()
DISCORD_TOKEN = os.getenv("DISCORD_TOKEN")

# Google Sheets setup
SHEET_NAME = "Expenses"
SCOPES = ["https://www.googleapis.com/auth/spreadsheets"]
creds = Credentials.from_service_account_file("credentials.json", scopes=SCOPES)
gc = gspread.authorize(creds)
SPREADSHEET_ID = "1byAJmNMWJ4ne69XUkvBSDHXK8NIoAlXvQhB6gU1uzXY"  # replace with your actual ID
sheet = gc.open_by_key(SPREADSHEET_ID).sheet1# Assumes you want the first worksheet

# Discord bot setup
intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f"Logged in as {bot.user}")

@bot.event
async def on_message(message):
    if message.author.bot:
        return

    # Find the first number in the message (integer or decimal)
    match = re.search(r"(\d+(\.\d+)?)", message.content)
    if match:
        amount = match.group(1)
        # Remove the amount from the message to get the description
        description = message.content.replace(amount, "", 1).strip()
        if not description:
            description = "No description"

        # Prepare data
        date_str = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        user = str(message.author)
        row = [date_str, user, amount, description]

        # Append to Google Sheet
        try:
            sheet.append_row(row)
            await message.channel.send(f"Expense logged: {amount} ({description})")
        except Exception as e:
            await message.channel.send(f"Failed to log expense: {e}")

    await bot.process_commands(message)

if __name__ == "__main__":
    bot.run(DISCORD_TOKEN)