from discord.ext import commands
import discord
import logging
from util import *
from pathlib import Path

logger = logging.getLogger(__name__)

class Meta(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='reload', description="reloads a cog")
    @commands.check_any(commands.is_owner())
    async def reload(self, ctx, arg):
        """
        reloads cog for when you test the bot in production :sunglas:
        """
        usage = ">reload {arg}"
        if len(arg) != 0:
            if arg.lower() == "all":
                cogs = [x.stem for x in Path('cogs').glob('*.py')]
            else:
                cogs = [arg]
            for cog in cogs:
                msg = await ctx.send(f"reloading cog {cog} {EMOTE_AF}")
                logger.info("reloading " + cog)
                try:
                    self.bot.reload_extension(f"cogs.{cog}")
                    await msg.edit(content=f"reloaded {EMOTE_AF}")
                except Exception as e:
                    await msg.edit(content=f"failed to reload {cog} {EMOTE_AF}")
                    logger.error(f"error {e}")
        else:
            await ctx.send(usage)

def setup(bot):
    bot.add_cog(Meta(bot))