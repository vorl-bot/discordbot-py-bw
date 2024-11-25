from cmath import log
from distutils.sysconfig import PREFIX
import discord
from dotenv import load_dotenv
import os
load_dotenv()
import random
import gacha
import soriziller
import omikuji
import arcade

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

    #연챠
    if message.content.startswith(f'{PREFIX}연챠'):
        ncha_result = gacha.nGacha()
        ncha_message = '삐롱삐롱삐로롱~ \n<'+ncha_result[0]+'>,\n<'+ncha_result[1]+'>,\n<'+ncha_result[2]+'>,\n<'+ncha_result[3]+'>,\n<'+ncha_result[4]+'>이(가) 나왔다!'
        await message.channel.send(ncha_message, reference=message)

    #동전
    if message.content.startswith(f'{PREFIX}동전'):
        c = random.choice(['앞면','뒷면'])
        embed=discord.Embed(description=":coin:팅그르르...",
                            color=0x008083)
        embed.add_field(name=c, value=" ", inline=False)
        await message.channel.send(embed=embed, reference=message)

    #다이스(1d100)
    if message.content.startswith(f'{PREFIX}다이스'):
        d = random.randrange(1,101)
        embed = discord.Embed(description=":game_die:도르르륵...",
                            color=0x008083)
        embed.add_field(name=d, value=" ", inline=False)
        await message.channel.send(embed=embed, reference=message)

    #노래방
    if message.content.startswith(f'{PREFIX}노래방'):
       noreabang = soriziller.soriziller()
       SongText = noreabang[0]
       SongText2 = noreabang[1]
       embed = discord.Embed(description=":mirror_ball:점수는! 두구두구…",
                            color=0x008083)
       embed.add_field(name=SongText, value=SongText2, inline=False)
       await message.channel.send(embed=embed, reference=message)

    #운세
    if message.content.startswith(f'{PREFIX}운세'):
       lucktest = omikuji.omikuji()
       omikujiText = lucktest[0]
       omikujiText2 = lucktest[1]
       embed = discord.Embed(description=":red_envelope:오늘의 운세!",
                            color=0x008083)
       embed.add_field(name=omikujiText, value=omikujiText2, inline=False)
       await message.channel.send(embed=embed, reference=message)

    #특수가챠
    if message.content.startswith(f'{PREFIX}특챠'):
        special = gacha.specialGacha()

        if len(special) == 3:
            embed=discord.Embed(title="달각달각달각달각······.", 
                                description="기계 안에서 캡슐이 나왔다! 캡슐을 열어보면·······.", 
                                color=0x008083)
            embed.add_field(name="", value='「'+special[0]+"」이(가) 나왔다. 인형에 딱 맞을 것 같은 사이즈네!", inline=False)
            embed.set_image(url=special[1])
            await message.channel.send(embed=embed, reference=message)

        if len(special) == 2:
            embed=discord.Embed(title="달각달각달각달각······.", 
                                description="기계 안에서 캡슐이 나왔다! 캡슐을 열어보면·······.", 
                                color=0x008083)
            embed.add_field(name="", value='《'+special[0]+"》이(가) 나왔다.\n"+special[1], inline=False)
            await message.channel.send(embed=embed, reference=message)

        if len(special) == 1:
            embed=discord.Embed(title="달각달각달각달각······.", 
                                description="기계 안에서 캡슐이 나왔다! 캡슐을 열어보면·······.", 
                                color=0x008083)
            embed.add_field(name="", value='<'+special[0]+">이(가) 나왔다.", inline=False)
            await message.channel.send(embed=embed, reference=message)

    #오락실
    #하이로우
    if message.content.startswith(f'{PREFIX}배팅'):

        embed=discord.Embed(title=":moneybag:배팅!",
                            description="높은 수일까, 낮은 수일까? 결과는...",
                            color=0x008083)
        embed.add_field(name=random.randrange(1,51), value='', inline=False)
        await message.channel.send(embed=embed, reference=message)
    
    #가위바위보
    if message.content.startswith(f'{PREFIX}가위바위보'):
        rsp = arcade.RSP()
        
        embed=discord.Embed(title=":vs:대결!", 
                            description="안 내면 진 거! 가위 바위 보!", 
                            color=0x008083)
        embed.add_field(name=rsp, value="", inline=False)
        await message.channel.send(embed=embed, reference=message)
    #가위바위보 컴이랑 뜨기
    if message.content.startswith(f'{PREFIX}대결'):
        rspVS = arcade.RSP_Com()
        VSText = rspVS[0]
        VSText2 = rspVS[1]
        VSText3 = rspVS[2]

        embed=discord.Embed(title=":vs:대결!", 
                            description=" ", 
                            color=0x008083)
        embed.add_field(name="헥스 vs Ai퐁당", value= VSText + '를 냈다. \n Ai퐁당이 ' + VSText2 + '를 냈다.', inline=False)
        embed.add_field(name="결과는?!", value=VSText3, inline=False)
        await message.channel.send(embed=embed, reference=message)

    #사격게임
    if message.content.startswith(f'{PREFIX}게임시작'):
        shotgame = arcade.ZombieGame()
        shottext = shotgame[0]
        shottext2 = shotgame[1]
        embed=discord.Embed(title=":syringe:리빙온더데드", 
                            description="좀비들을 피해서 백신을 구해오자!", 
                            color=0x008083)
        embed.add_field(name='GAME START!', value="탕! 탕! 나타나는 좀비들을 처치하며 연구소로 향했다. \n . \n . \n . ", inline=False)
        embed.add_field(name=shottext2, value=shottext, inline=False)
        await message.channel.send(embed=embed, reference=message)

    #슬롯머신
    if message.content.startswith(f'{PREFIX}슬롯머신'):
        SM = arcade.SlotMachine()
        
        embed = discord.Embed(description=":slot_machine:",
                            color=0x008083)
        embed.add_field(name=SM, value=" ", inline=False)
        await message.channel.send(embed=embed, reference=message)



try:
    client.run(TOKEN)
except discord.errors.LoginFailure as e:
    print("Improper token has been passed.")


"""
#첫번째 마그눔 오푸스

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

#마그눔오푸스2
    #물풍선낚시
    if message.content.startswith(f'{PREFIX}물풍선'):
        yoyo = magnum2.yoyotsuri()
        yoyotext = yoyo[0]
        yoyotext2 = yoyo[1]
        embed=discord.Embed(title=":bubbles:물풍선낚시!", 
                            description="조심조심······. 가는 종이를 돌려 만들어진 낚싯대를 들고 물풍선의 고리를 낚싯대에 걸어 물풍선을 건져보자.", 
                            color=0x52ebff)
        embed.add_field(name=yoyotext, value=yoyotext2, inline=False)
        await message.channel.send(embed=embed, reference=message)
    #사격게임
    if message.content.startswith(f'{PREFIX}사격'):
        shotgame = magnum2.shot()
        shottext = shotgame[0]
        shottext2 = shotgame[1]
        shottext3 = shotgame[2]
        embed=discord.Embed(title=":gun:사격게임", 
                            description="기회는 5번! 준비하시고~ 쏘세요!", 
                            color=0x6D4948)
        embed.add_field(name='빵야!', value=shottext, inline=False)
        embed.add_field(name=shottext2, value=shottext3, inline=False)
        await message.channel.send(embed=embed, reference=message)
    #비밀메뉴
    if message.content.startswith(f'{PREFIX}비밀메뉴'):
        SMenu = magnum2.SecretMenu()
        embed=discord.Embed(title=":fork_knife_plate:비밀 메뉴 찾기!", 
                            description="비밀 메뉴를 찾아보자!", 
                            color=0x008083)
        embed.add_field(name='첫 번째 힌트는?', value=SMenu, inline=False)
        await message.channel.send(embed=embed, reference=message)

    #RGB요리사
    #주방
    if message.content.startswith(f'{PREFIX}주방'):
       KitchenDraw = magnum2.Kitchen()
       embed = discord.Embed(description="주방에서 찾아낸 요리 재료는……",
                            color=0xED4245)
       embed.add_field(name=KitchenDraw, value='', inline=False)
       await message.channel.send(embed=embed, reference=message)
    #온실
    if message.content.startswith(f'{PREFIX}온실'):
       GardenDraw = magnum2.Greenhouse()
       embed = discord.Embed(description="온실에서 찾아낸 요리 재료는……",
                            color=0x57F287)
       embed.add_field(name=GardenDraw, value='', inline=False)
       await message.channel.send(embed=embed, reference=message)
    #인공호수
    if message.content.startswith(f'{PREFIX}인공호수'):
       LakeDraw = magnum2.Lake()
       embed = discord.Embed(description="인공호수에서 찾아낸 요리 재료는……",
                            color=0x3498DB)
       embed.add_field(name=LakeDraw, value='', inline=False)
       await message.channel.send(embed=embed, reference=message)
    #조미료
    if message.content.startswith(f'{PREFIX}조미료'):
       SeasoningDraw = magnum2.Seasoning()
       embed = discord.Embed(description="손에 쥐여진 조미료는……",
                            color=0xFFFFFF)
       embed.add_field(name=SeasoningDraw, value='', inline=False)
       await message.channel.send(embed=embed, reference=message)
    #방청객
    if message.content.startswith(f'{PREFIX}점수권'):
       ChanceDraw = magnum2.Audience()
       CDrawText = ChanceDraw[0]
       CDrawText2 = ChanceDraw[1]
       embed = discord.Embed(description="뒤적뒤적뒤적… 종이가 잡혔다!",
                            color=0x1ABC9C)
       embed.add_field(name=CDrawText, value=CDrawText2, inline=False)
       await message.channel.send(embed=embed, reference=message)


"""
"""
    #세번째 마그눔오푸스
    #실뽑기
    if message.content.startswith(f'{PREFIX}물레'):
        thread = magnum3.spinning()
        text1 = thread[0]
        text2 = thread[1]

        embed=discord.Embed(title=":yarn:실 잣기!", 
                            description="드르륵 드르륵... 물레를 돌려 양털에서 실을 뽑아내자.", 
                            color=0xc670ff)
        embed.add_field(name=text1, value=text2, inline=False)
        await message.channel.send(embed=embed, reference=message)

    #천짜기
    if message.content.startswith(f'{PREFIX}베틀'):
        fabric = magnum3.weaving()
        text1 = fabric[0]
        text2 = fabric[1]

        embed=discord.Embed(title=":thread:옷감 짜기!", 
                            description="드르륵 드르륵... 뽑아낸 실로 베틀에서 옷감을 짜 보자.", 
                            color=0xff707e)
        embed.add_field(name=text1, value=text2, inline=False)
        await message.channel.send(embed=embed, reference=message)

    #감정
    if message.content.startswith(f'{PREFIX}감정'):
        valued = magnum3.valuation()
        
        embed=discord.Embed(title=":mag:이 물건의 가치는?", 
                            description="골동품점에서 찾아낸 물건을 유심히 들여다보자. 나의 예측이 맞았을까? \n 이 물건의 실제 가치는...", 
                            color=0x70fff5)
        embed.add_field(name=valued, value="", inline=False)
        await message.channel.send(embed=embed, reference=message)

    #미션
    if message.content.startswith(f'{PREFIX}미션'):
        mission = magnum3.Mission()
        
        embed=discord.Embed(title=":bangbang:미션!", 
                            description="다음의 미션을 수행하라.", 
                            color=0xffffff)
        embed.add_field(name=mission, value="", inline=False)
        await message.channel.send(embed=embed, reference=message)  

    #공격
    if message.content.startswith(f'{PREFIX}공격'):
        ATK = magnum3.Attack()
        text1 = ATK[0]
        text2 = ATK[1]

        embed=discord.Embed(title=":crossed_swords:공격!", 
                            description=text1, 
                            color=0xff2e2e)
        embed.add_field(name=text2, value="", inline=False)
        await message.channel.send(embed=embed, reference=message)

    #방어
    if message.content.startswith(f'{PREFIX}방어'):
        DFC = magnum3.Defence()
        text1 = DFC[0]
        text2 = DFC[1]

        embed=discord.Embed(title=":shield:방어!", 
                            description=text1, 
                            color=0x2e3cff)
        embed.add_field(name=text2, value="", inline=False)
        await message.channel.send(embed=embed, reference=message)    

    #아이템
    if message.content.startswith(f'{PREFIX}아이템'):
        ITM = magnum3.Item()
        text1 = ITM[0]
        text2 = ITM[1]

        embed=discord.Embed(title=":gem:아이템을 획득했다!", 
                            description='', 
                            color=0x2eff58)
        embed.add_field(name=text1, value=text2, inline=False)
        await message.channel.send(embed=embed, reference=message)    

    #드랍
    if message.content.startswith(f'{PREFIX}우동'):
        DRP = magnum3.ItemDrop()
        await message.channel.send(DRP, reference=message) 

"""
