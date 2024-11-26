import discord
from discord.ext import commands, tasks
from datetime import datetime, timedelta

class reminder(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="r", description="remind meeting attendance")
    async def add_meeting(self, ctx):
        print ("command r fired")
        tokens = ctx.message.content.split()
        print(tokens)
        await ctx.send(("joe mama"))

async def setup(bot):
    await bot.add_cog(reminder(bot))
