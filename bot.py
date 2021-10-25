import asyncio
import discord
from discord.ext import tasks, commands
import os
import logging
from pathlib import Path
from discord.ext.commands.core import bot_has_permissions, command
from dotenv import load_dotenv

load_dotenv()
BOT_TOKEN = os.getenv("BOT_TOKEN")
BOT_PREFIX = ">"

class Bot(commands.Bot):
    
    def __init__(self):
        super().__init__(
            command_prefix=BOT_PREFIX,
            help_command=None
            )
        self.load_extensions()

    def load_extensions(self):
        cogs = [x.stem for x in Path('cogs').glob('*.py')]
        for extension in cogs:
            try:
                self.load_extension(f'cogs.{extension}')
                print(f'loading {extension}')
            except Exception as e:
                error = f'{extension}\n {type(e).__name__} : {e}'
                print(f'failed to load {error}')
            print('-' * 10)
        

async def run():
    bot = Bot()
    try:
        await bot.start(BOT_TOKEN)
    except KeyboardInterrupt:
        await bot.logout()

logging.basicConfig(level=logging.INFO)
logging.getLogger("requests").setLevel(logging.WARNING)
loop = asyncio.get_event_loop()
loop.run_until_complete(run())