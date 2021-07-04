import discord
import os
TOKEN = os.getenv("token")
PREFIX = 'fb.'
INTENTS = discord.Intents.default()
client = discord.Client(commands_prefix=PREFIX, intents=INTENTS)


@client.event
async def on_ready():
    print(f'Logged in as: {client.user.name}')
    print(f'With ID: {client.user.id}')
    logchannel = client.get_channel(id=802882486090072104)
    await logchannel.send("Test Bot Started")


client.run(TOKEN)