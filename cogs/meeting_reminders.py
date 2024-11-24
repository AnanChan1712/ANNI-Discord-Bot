import discord
from discord.ext import commands, tasks
from datetime import datetime, timedelta

class MeetingReminder(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.meetings = []  # Storing meeting details
        self.check_meetings.start()

    @commands.command(name="brain trust meeting")
    async def add_meeting(self, ctx, time: str, *, description: str):
        """
        Add a meeting.
        Format for time: YYYY-MM-DD HH:MM (24-hour format)
        Example: !add_meeting 2024-11-19 19:30 Team discussion
        """
        try:
            meeting_time = datetime.strptime(time, "%Y-%m-%d %H:%M")
            self.meetings.append({"time": meeting_time, "description": description, "channel": ctx.channel.id})
            await ctx.send(f"Meeting added: {description} at {meeting_time}")
        except ValueError:
            await ctx.send("Invalid time format! Use YYYY-MM-DD HH:MM.")

    @commands.command(name="list_meetings")
    async def list_meetings(self, ctx):
        """List all upcoming meetings."""
        if not self.meetings:
            await ctx.send("No upcoming meetings!")
            return
        
        sorted_meetings = sorted(self.meetings, key=lambda x: x["time"])
        message = "\n".join([f"{m['time']} - {m['description']}" for m in sorted_meetings])
        await ctx.send(f"Upcoming meetings:\n{message}")

    @tasks.loop(seconds=60)  # Check every minute
    async def check_meetings(self):
        now = datetime.now()
        for meeting in self.meetings:
            if meeting["time"] <= now:
                channel = self.bot.get_channel(meeting["channel"])
                if channel:
                    await channel.send(f"Reminder: {meeting['description']} is happening now!")
                self.meetings.remove(meeting)

    @check_meetings.before_loop
    async def before_check_meetings(self):
        await self.bot.wait_until_ready()

def setup(bot):
    bot.add_cog(MeetingReminder(bot))
