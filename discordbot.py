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
    
        if message.content.startswith(f'{PREFIX}명령어'):
            embed=discord.Embed(title="!명령어", description="아래의 명령어를 입력해보세요!!", color=0xff0000)  
            embed.add_field(name="!행운", value="행운을 올려보세요!", inline=False)
            embed.add_field(name="!가이드북", value="가이드북 주소를 알려드려요!", inline=False)
            embed.add_field(name="!패치파일", value="패치파일 주소를 알려드려요!", inline=False)
            embed.add_field(name="!천사날개 조합식", value="천사날개 조합식을 알려드려요!", inline=False)
            embed.add_field(name="!알파윙 조합식", value="알파윙 조합식을 알려드려요!", inline=False)
            embed.add_field(name="!진알파 조합식", value="진알파 조합식을 알려드려요!", inline=False)
            embed.add_field(name="!케루빔 조합식", value="케루빔 조합식을 알려드려요!", inline=False)
            await client.send_message(channel,embed=embed)

    if message.content.startswith(f'{PREFIX}행운'):
        await message.channel.send(message.author.name +"님 오늘은 좋은걸 얻을거 같아요!!")

    if message.content.startswith(f'{PREFIX}가이드북'):
        await message.channel.send('https://cafe.naver.com/twguide/2?boardType=L')
        
    if message.content.startswith(f'{PREFIX}패치파일'):
        await message.channel.send('https://drive.google.com/file/d/1wN9usx5rJm0fIXcba2cXDIyJMqrjFFib/view?usp=sharing')
        
    if message.content.startswith(f'{PREFIX}!알파윙 조합식'):
        await channel.send("```리틀 그레스 윙 3합\n에메랄드 20개\n천공의 깃털 20개```")

    if message.content.startswith(f'{PREFIX}!천사날개 조합식'):
        await channel.send("```리틀 플라티나 윙 3합\n에메랄드 20개\n천공의 깃털 20개```")

    if message.content.startswith(f'{PREFIX}!진알파 조합식'):
        await channel.send("```알파 윙 3합 1개\n흑해진보 40개\n쿠로이 깃털 1개```")

    if message.content.startswith(f'{PREFIX}!케루빔 조합식'):
         await channel.send("```천사날개 3합 1개\n흑해진보 40개\n쿠로이 깃털 1개```")

try:
    client.run(TOKEN)
except discord.errors.LoginFailure as e:
    print("Improper token has been passed.")
