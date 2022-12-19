from cmath import log
from distutils.sysconfig import PREFIX
import discord
from dotenv import load_dotenv
import os
load_dotenv()

PREFIX = os.environ['PREFIX']
TOKEN = os.environ['TOKEN']

client = discord.Client()

@client.event
async def on_ready():
    print(f'Logged in as {client.user}.')

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content == f'{PREFIX}행운':
        await channel.send(message.author.name +'님 오늘은 좋은걸 얻을거 같아요!!')

    if message.content.startswith(f'{PREFIX}가이드북'):
        await message.channel.send('await channel.send("https://cafe.naver.com/twguide/2?boardType=L")')


try:
    client.run(TOKEN)
except discord.errors.LoginFailure as e:
    print("Improper token has been passed.")
