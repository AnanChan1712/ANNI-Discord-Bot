import discord
from discord.ext import commands, tasks
from datetime import datetime, timedelta
import yaml
import utils.helpers as helpers
#object-oriented approach for Linux (utils.helpers) --> "as helpers" to easily mention 

def load_config(file_path="link.yaml"):
    with open(file_path, "r") as file:
        return yaml.safe_load(file)
    
class reminder(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="meet", description="remind meeting attendance")
    async def add_meeting(self, ctx):
        tokens = ctx.message.content.split()
        data =""

#not sure of this line's purpose, possibly to acess the yaml file?
        config_data = helpers.loadCache("link.yaml","reminder")
        print("hi theretmlxwkxrer" + str(config_data))
#file = txt document, directory=folder

        if len(tokens) == 1:
            data = "Usage: !meet [bt or l]\nOptions:\n  'bt' -> Brain Trust\n  'l' -> Leadership Meeting"

        elif len(tokens) == 2:
            if tokens[1] == "bt":
                bt = config_data["bt"]
                data = (
                    "@everyone Brain Trust starting now!\n"
                    f"Join here:{bt}"
                )
            elif tokens[1] == "l":
                l = config_data["l"]
                data = (
                    "@everyone Brain Trust starting now!\n"
                    f"Join here:{l}"
                )
            else:
                data = "Unknown meeting type. Use 'bt' or 'l'."

        # If too many arguments are provided
        else:
            data = "Too many arguments. Usage: !meet [bt or l]"

        await ctx.send(data)
        #ctx = a class that has access to all the server's discord data (guild)

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
