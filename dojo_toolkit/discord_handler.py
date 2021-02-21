import asyncio
import threading
import os

import discord

DISCORD_TOKEN = os.getenv('TOKEN')
client = discord.Client()


async def send_message(message):
    print('sendou message')
    await asyncio.sleep(2)
    print('top', message)
    # channel = client.get_channel(os.getenv('ID'))
    # await channel.send(message)


def foo():
    import time
    print('foo')
    time.sleep(2)
    client.loop.create_task(send_message('show'))
    client.loop.create_task(send_message('top'))
    client.loop.create_task(send_message('pot'))


thread = threading.Thread(target=foo)
thread.start()

client.run(DISCORD_TOKEN)
