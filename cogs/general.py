from util import *
from Crypto.Util.number import long_to_bytes, bytes_to_long
from discord.ext import commands
from discord.utils import escape_mentions
import logging

class General(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='l2b', aliases=['longtobytes', 'long_to_bytes'])
    async def l2b(self, ctx, *args):
        """
        converts a base-10 integer into a byte string. the most useful function ever
        """
        sent = False
        args = parsemessage(args)
        for arg in args:
            try:
                ret = escape_markdown(escape_mentions(str(long_to_bytes(int(arg))))[2:-1])
                await ctx.send(ret)
                sent = True
            except:
                pass
        if not sent:
            await ctx.send(ERROR_MSG_GENERIC)

    @commands.command(name='b2l', aliases=['bytestolong', 'bytes_to_long'])
    async def b2l(self, ctx, *args):
        """
        converts a byte string into a base-10 integer
        """
        args = " ".join(args)
        try:
            ret = bytes_to_long(args.encode())
            await ctx.send(ret)
        except Exception as e:
            await ctx.send(ERROR_MESSAGE_GENERIC)

    @commands.command(name='unhex', aliases=['uhex'])
    async def hex_decode(self, ctx, *args):
        """
        converts a hexadecimal string to a byte string
        """
        truncated = False
        sent = False
        args = parsemessage(args)
        for arg in args:
            arg = arg.replace("0x", "")
            if len(arg) % 2 and truncated:
                arg = arg[:-1]
                await ctx.send(f"note: one or more of your hex strings had an odd number of hex digits")
                truncated = True
            try:
                ret = escape_markdown(escape_mentions(str(bytes.fromhex(arg))[2:-1]))
                await ctx.send(ret)
                sent = True
            except:
                pass
        if not sent:
            await ctx.send(ERROR_MESSAGE_GENERIC)


def setup(bot):
    bot.add_cog(General(bot))
