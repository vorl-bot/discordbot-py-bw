from cmath import log
from distutils.sysconfig import PREFIX
import discord
from dotenv import load_dotenv
import os
load_dotenv()
import random
import gacha
import magnum1

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

    if message.content == f'{PREFIX}call':
        await message.channel.send("callback!")

    if message.content.startswith(f'{PREFIX}hello'):
        await message.channel.send('Hello!', reference=message)

    #가챠
    if message.content.startswith(f'{PREFIX}가챠'):
        gacha_result = gacha.getGacha()
        gacha_message = '삐로로롱~ <'+gacha_result+'>이(가) 나왔다!'
        await message.channel.send(gacha_message, reference=message)

    #동전
    if message.content.startswith(f'{PREFIX}동전'):
        c = random.choice(['앞면','뒷면'])
        embed=discord.Embed(description=":coin:팅그르르...",
                            color=0x61b866)
        embed.add_field(name=c, value=" ", inline=False)
        await message.channel.send(embed=embed, reference=message)

    #다이스(1d100)
    if message.content.startswith(f'{PREFIX}다이스'):
        d = random.randrange(1,101)
        embed = discord.Embed(description=":game_die:도르르륵...",
                            color=0x000000)
        embed.add_field(name=d, value=" ", inline=False)
        await message.channel.send(embed=embed, reference=message)

    #혜윰미니게임
    if message.content.startswith(f'{PREFIX}단어'):
        word = magnum1.hyeyum()
        from datetime import datetime
        dt = datetime.now()
        dtfinalminute = int(dt.strftime('%M'))+2

        embed=discord.Embed(title=":pencil:공용어 퀴즈!", 
                            description="다음의 초성으로 시작하는 단어를 3개 제시하시오.\n 제한시간: "+dt.strftime('%Y년 %m월 %d일 %H시 ')+dtfinalminute+'분 '+dt.strftime('%S초까지'), 
                            color=0xf1c232)
        embed.add_field(name=word, value="", inline=False)
        await message.channel.send(embed=embed, reference=message)


try:
    client.run(TOKEN)
except discord.errors.LoginFailure as e:
    print("Improper token has been passed.")