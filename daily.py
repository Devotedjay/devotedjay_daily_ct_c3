import discord
import asyncio
import datetime
import os

TOKEN = os.getenv("DISCORD_TOKEN")
CHANNEL_ID = int(os.getenv("DISCORD_CHANNEL_ID"))

class MyClient(discord.Client):
    async def on_ready(self):
        target_date = datetime.date(2026, 6, 1)
        today = datetime.date.today()
        delta = (target_date - today).days
        channel = self.get_channel(CHANNEL_ID)
        if channel:
            await channel.send(f"📅 Còn {delta} ngày nữa đến ngày 01/06/2026!")
        await self.close()

intents = discord.Intents.default()
client = MyClient(intents=intents)
asyncio.run(client.start(TOKEN))
