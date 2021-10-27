from discord.ext import commands
import discord
import logging
from util import *

logger = logging.getLogger(__name__)

class RSA(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    # main things: automatic sagecell script generator, trivial attacks, check for factordb etc

    
def setup(bot):
    bot.add_cog(RSA(bot))