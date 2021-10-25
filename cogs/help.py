from discord.ext import commands
import discord
import logging

class Base(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='help', description="shows this help message")
    async def help_command(self, ctx):
        await ctx.send("please send help")

def setup(bot):
    bot.add_cog(Base(bot))
