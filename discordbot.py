from cmath import log
from distutils.sysconfig import PREFIX
import discord
from dotenv import load_dotenv
import os
load_dotenv()
import random
import gacha
import magnum1

from datetime import datetime
from pytz import timezone

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
        dt = datetime.now((timezone('Asia/Seoul')))
        dtfinalhour = int(dt.strftime('%H'))
        dtfinalminute = int(dt.strftime('%M'))+2
        if dtfinalminute > 59:
            dtfinalminute = dtfinalminute - 60
            dtfinalhour = dtfinalhour +1
            if dtfinalhour >= 24:
                dtfinalhour = dtfinalhour - 24

        embed=discord.Embed(title=":pencil:공용어 퀴즈!", 
                            description='다음의 초성으로 시작하는 단어를 5개 제시하시오.\n 제한시간: '+str(dtfinalhour)+'시 '+str(dtfinalminute)+'분까지', 
                            color=0xf1c232)
        embed.add_field(name=word, value="", inline=False)
        await message.channel.send(embed=embed, reference=message)

    #벨체르미니게임
    if message.content.startswith(f'{PREFIX}양털'):
        lamb = magnum1.belcher()
        text1 = lamb[0]
        text2 = lamb[1]

        embed=discord.Embed(title=":sheep:양털깎기!", 
                            description="양털을 깎고 퐁당이를 구출하자. 싹둑싹둑...", 
                            color=0x6aa84f)
        embed.add_field(name=text1, value=text2, inline=False)
        await message.channel.send(embed=embed, reference=message)

    #로테폴미니게임
    if message.content.startswith(f'{PREFIX}숫자'):
        calc = magnum1.rhotepol()
        calc1 = calc[0]
        calc2 = calc[1]

        embed=discord.Embed(title=":abacus:사칙연산!", 
                            description="제시된 숫자 또는 부호를 모두 사용해 수식을 만들어보자.\n 계산한 값이 0이 되는 수식을 완성하면 성공! ", 
                            color=0x2d4799)
        embed.add_field(name=calc1, value="", inline=True)
        embed.add_field(name=calc2, value="", inline=True)
        await message.channel.send(embed=embed, reference=message)

try:
    client.run(TOKEN)
except discord.errors.LoginFailure as e:
    print("Improper token has been passed.")