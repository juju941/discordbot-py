from cmath import log
from distutils.sysconfig import PREFIX
import discord
from dotenv import load_dotenv
import os
import random
load_dotenv()

PREFIX = os.environ['PREFIX']
TOKEN = os.environ['TOKEN']

intents=discord.Intents.all()
client=discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'Logged in as {client.user}.')
    await client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name='난 뚜뚜킹이야 !명령어를 입력해봐 !!'))
                      
@client.event
async def on_member_join(member):
    print("member join")
    channel = client.get_channel(1068455687564316762)
    welcomembed=discord.Embed(title="환-영", description=f"{member.name}님", color=0xffae00)
    await channel.send(f"{member.mention}님, 암명서버에 어서오세요!")
    
@client.event
async def on_message(message):
    
    if message.content.startswith(f'{PREFIX}명령어'):
        embed=discord.Embed(title="!명령어", description="아래의 명령어를 입력해보세요!!", color=0xff0000)  
        embed.add_field(name="!행운", value="행운을 올려보세요!", inline=False)
        embed.add_field(name="!가이드북", value="가이드북 주소를 알려드려요!", inline=False)
        embed.add_field(name="!패치파일", value="패치파일 주소를 알려드려요!", inline=False)
        embed.add_field(name="!천사날개 조합식", value="천사날개 조합식을 알려드려요!", inline=False)
        embed.add_field(name="!알파윙 조합식", value="알파윙 조합식을 알려드려요!", inline=False)
        embed.add_field(name="!진알파 조합식", value="진알파 조합식을 알려드려요!", inline=False)
        embed.add_field(name="!암대천 조합식", value="암대천 조합식을 알려드려요!", inline=False)
        await message.channel.send(embed=embed)

    if message.content.startswith(f'{PREFIX}행운'):
        embed=discord.Embed(title="행운 올려보기", description=message.author.name +"님 오늘은 좋은걸 얻을거 같아요!!", color=0xffae00)
        await message.channel.send(embed=embed)

    if message.content.startswith(f'{PREFIX}가이드북'):
        embed=discord.Embed(title="가이드북 바로가기", description="[바로가기](https://cafe.naver.com/twguide/2?boardType=L) \n링크를 클릭하시면 바로 이동합니다.", color=0x4df038)
        embed.set_footer(text="MADE BY 빛/신")
        await message.channel.send(embed=embed)
        
    if message.content.startswith(f'{PREFIX}패치파일'):
        embed=discord.Embed(title="패치파일 바로가기", description="[바로가기](https://drive.google.com/file/d/1wN9usx5rJm0fIXcba2cXDIyJMqrjFFib/view?usp=sharing) \n링크를 클릭하시면 바로 이동합니다.", color=0x4df038)
        await message.channel.send(embed=embed)
        
    if message.content.startswith(f'{PREFIX}알파윙 조합식'):
        embed=discord.Embed(title="알파윙 조합식", description="리틀 그레스 윙 3합\n에메랄드 20개\n천공의 깃털 20개", color=0x9fbcfe)
        await message.channel.send(embed=embed)

    if message.content.startswith(f'{PREFIX}천사날개 조합식'):
        embed=discord.Embed(title="천사날개 조합식", description="리틀 플라티나 윙 3합\n에메랄드 20개\n천공의 깃털 20개", color=0x9fd5fe)
        await message.channel.send(embed=embed)
                            
    if message.content.startswith(f'{PREFIX}진알파 조합식'):
        embed=discord.Embed(title="진알파 조합식", description="알파 윙 3합 1개\n흑해진보 40개\n쿠로이 깃털 1개", color=0x5385ea)
        await message.channel.send(embed=embed)

    if message.content.startswith(f'{PREFIX}암대천 조합식'):
        embed=discord.Embed(title="암대천 조합식", description="천사날개 3합 1개\n흑해진보 40개\n쿠로이 깃털 1개", color=0xa9aeb7)
        await message.channel.send(embed=embed)

try:
    client.run(TOKEN)
except discord.errors.LoginFailure as e:
    print("Improper token has been passed.")
