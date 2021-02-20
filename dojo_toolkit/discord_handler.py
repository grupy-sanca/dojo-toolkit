import os

import discord

client = discord.Client()

async def send_message(message):
    channel = client.get_channel(os.getenv('ID'))
    await channeld.send(message)


client.run(os.getenv('TOKEN'))