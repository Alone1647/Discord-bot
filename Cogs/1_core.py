import disnake
from disnake.ext import commands
import requests
import json

client_id = "TikMmw1Tk3I8YAmbAXIb"
client_secret = "79SyD7Wwo0"


class core(commands.Cog):
    def __init__(self,bot):
        self.bot = bot
    
    @commands.command(name = "출력")
    async def _print(ctx):
        await ctx.message.reaction("✅")
        await ctx.send("파이썬에 의해 출력됨")

def setup(bot):
    bot.add_cog(core(bot))