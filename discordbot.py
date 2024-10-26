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
        calc1 = magnum1.rhotepol()
        calc2 = magnum1.rhotepol()

        calc_result = calc1 + '  '+calc2

        embed=discord.Embed(title=":abacus:사칙연산!", 
                            description="제시된 숫자 또는 부호를 모두 사용해 수식을 만들어보자.\n 계산한 값이 0이 되는 수식을 완성하면 성공! ", 
                            color=0x2d4799)
        embed.add_field(name=calc_result, value='', inline=True)
        await message.channel.send(embed=embed, reference=message)

    #나이라미니게임
    if message.content.startswith(f'{PREFIX}배팅'):

        embed=discord.Embed(title=":moneybag:배팅!",
                            description="높은 수일까, 낮은 수일까? 결과는...",
                            color=0x8c2b3f)
        embed.add_field(name=random.randrange(1,51), value='', inline=False)
        await message.channel.send(embed=embed, reference=message)

    #사금채취
    if message.content.startswith(f'{PREFIX}사금'):
        gold = random.choice(['『사금』이 채취되었다! ','『모래』 뿐이다·····!'])

        embed=discord.Embed(title=":star2:일확천금 사금채취!", 
                            description='찰랑찰랑찰랑····. 수조 안에 든 모래를 퍼올리고, 다시 접시를 물에 가라앉혀 모래를 흘려보내면······.', 
                            color=0xf1c232)
        embed.add_field(name=gold, value="", inline=False)
        await message.channel.send(embed=embed, reference=message)

    #도자기
    if message.content.startswith(f'{PREFIX}도자기'):
        ceramicNum = random.randrange(1,5)

        if ceramicNum == 1:
            ceramic = '으아아아아아악! 이건 「도자기…?」. 도자기라고 할 수 있을까?'
        
        elif ceramicNum == 2:
            ceramic = '「조금 미흡한 도자기」의 모습이 나왔다! 색을 얹고 장식을 하고 구워도 조금…미묘한 모양새이지만 괜찮으려나.'

        elif ceramicNum == 3:
            ceramic = '「괜찮은 도자기」의 모습이 나왔다! 색을 얹고 장식을 하고 구우면 괜찮을 거야!'

        elif ceramicNum == 4:
            ceramic = '「완벽한 도자기」의 모습이 나왔다! 색을 얹고 장식을 하고 구우면 완벽해!'
        

        embed=discord.Embed(title=":amphora:도자기를 만들자!", 
                            description='빙글빙글빙글······. 담당퐁당의 도움을 받아 흙을 얹고 물레를 돌린다. 집중하여 흙에 손을 얹고 물레를 돌리고 있으면····', 
                            color=0xffb0c0)
        embed.add_field(name=ceramic, value="", inline=False)
        await message.channel.send(embed=embed, reference=message)

    #통발
    if message.content.startswith(f'{PREFIX}통발'):
        fishNum = str(random.randrange(0,21))

        embed=discord.Embed(title=":fish:통발 낚시!", 
                            description="영차영차 통발을 건졌다. 몇 마리나 잡혔을까? 확인해보면...", 
                            color=0x2d4799)
        embed.add_field(name=fishNum+'마리를 잡았다!', value='', inline=True)
        await message.channel.send(embed=embed, reference=message)

    #운송게임
    if message.content.startswith(f'{PREFIX}운송'):
        trans = magnum1.transport()

        embed=discord.Embed(title=":camel:아트라프를 향해 출발!",
                            description=trans,
                            color=0x8c2b3f)
        embed.add_field(name='', value='', inline=False)
        await message.channel.send(embed=embed, reference=message)

    #특수가챠
    if message.content.startswith(f'{PREFIX}특챠'):
        special = gacha.specialGacha()

        if len(special) == 3:
            embed=discord.Embed(title="달각달각달각달각······.", 
                                description="기계 안에서 캡슐이 나왔다! 캡슐을 열어보면·······.", 
                                color=0x008083)
            embed.add_field(name="", value=special[0]+"이(가) 나왔다. 인형에 딱 맞을 것 같은 사이즈네!", inline=False)
            embed.set_image(url=special[1])
            await message.channel.send(embed=embed, reference=message)

        if len(special) == 1:
            embed=discord.Embed(title="달각달각달각달각······.", 
                                description="기계 안에서 캡슐이 나왔다! 캡슐을 열어보면·······.", 
                                color=0x008083)
            embed.add_field(name="", value=special+"이(가) 나왔다.", inline=False)
            await message.channel.send(embed=embed, reference=message)


try:
    client.run(TOKEN)
except discord.errors.LoginFailure as e:
    print("Improper token has been passed.")