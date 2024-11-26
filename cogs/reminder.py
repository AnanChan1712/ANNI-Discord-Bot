import discord
from discord.ext import commands, tasks
from datetime import datetime, timedelta

class reminder(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="meet", description="remind meeting attendance")
    async def add_meeting(self, ctx):
        tokens = ctx.message.content.split()
        data =""

        if len(tokens) == 1:
            data = "Usage: !meet [bt or l]\nOptions:\n  'bt' -> Brain Trust\n  'l' -> Leadership Meeting"

        elif len(tokens) == 2:
            if tokens[1] == "bt":
                data = (
                    "@everyone Brain Trust starting now!\n"
                    "Join here: https://us02web.zoom.us/j/88968536984?pwd=SGdwM1lFbmoraVE5eS9iR2NJNUJyUT09"
                )
            elif tokens[1] == "l":
                data = (
                    "@everyone Leadership Meeting starting now!\n"
                    "Join here: link loading..."
                )
            else:
                data = "Unknown meeting type. Use 'bt' or 'l'."

        # If too many arguments are provided
        else:
            data = "Too many arguments. Usage: !meet [bt or l]"

        await ctx.send(data)

        #formatted reminder:
        #message = (
         #   f"{meeting['tag']} {meeting['name']} starting now!\n"
          #  f"Join here: {meeting['link']}"
      #  )   
     #   await ctx.send(message)

      # print ("command r fired")
    #   tokens = ctx.message.content.split()
      #  print(tokens)
      #  await ctx.send(("joe"))

async def setup(bot):
    await bot.add_cog(reminder(bot))
