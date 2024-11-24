import random

Slots = [':number_7:',':joker:',':books:',':desert:',':park:',':ocean:',':bouquet:',':peacock:',':droplet:',':art:',
         ':maracas:',':game_die:',':flower_playing_cards:',':boom:',':apple:',':tangerine:',':onion:',':pizza:',':ice_cream:',':bulb:']

def SlotMachine():
    sFirst = random.choice(Slots)
    sSecond = random.choice(Slots)
    sThird = random.choice(Slots)

    Text = " "
    Text = Text + sFirst
    Text = Text + sSecond
    Text = Text + sThird

    return Text

def ZombieGame():

    shotscore1 = random.randrange(50,1001)
    
    if shotscore1 >= 100:
        shotscore2 = random.randrange(0,1001)
        sText3 = 'GAME OVER. 재장전 중 좀비에게 물려버렸다…….'
    elif shotscore1 < 100:
        shotscore2 = 0
        sText3 = 'GAME OVER. 좀비에게 물려버렸다…….'
 
    if shotscore2 >= 200:
        shotscore3 = random.randrange(0,1001)
        sText3 = 'GAME OVER. 연구실 안의 좀비에게 물려버렸다…….'
    elif shotscore2 < 200:
        shotscore3 = 0

    if shotscore3 >= 300:
        shotscore4 = random.randrange(0,1001)
        sText3 = 'GAME OVER. 최종 보스에게 패배했다…….'
    elif shotscore3 < 300:
        shotscore4 = 0

    if shotscore4 >= 500:
        shotscore5 = random.randrange(0,1001)
        sText3 = 'GAME CLEAR! 모든 스테이지를 클리어했다!'
    elif shotscore4 < 500:
        shotscore5 = 0

    totalscore = shotscore1+shotscore2+shotscore3+shotscore4+shotscore5

    sText2 = '최종 스코어는 '+str(totalscore)+'점!'

    return sText2, sText3

def RSP():

    RSPNum = random.randrange(0,101)
    RSPNum = RSPNum % 3

    if RSPNum == 0:
        text = '가위'
    elif RSPNum == 1:
        text = '바위'
    elif RSPNum == 2:
        text = '보'

    return text

def RSP_Com():

    PCNum = random.randrange(0,101)
    PCNum = PCNum % 3

    ComNum = random.randrange(0,101)
    ComNum = ComNum % 3

    WinText = "Ai퐁당에게 이겼다!"
    LoseText = "Ai퐁당에게 졌다!"
    DrawText = "Ai퐁당과 비겼다!"

    # 0 가위 / 1 바위 / 2 보
    
    if PCNum == 0:
        PCtext = '가위'
        if ComNum == 0:
            Comtext = '가위'
            Resulttext = DrawText
        elif ComNum == 1:
            Comtext = '바위'
            Resulttext = LoseText
        elif ComNum == 2:
            Comtext = '보'
            Resulttext = WinText
    elif PCNum == 1:
        PCtext = '바위'
        if ComNum == 0:
            Comtext = '가위'
            Resulttext = WinText
        elif ComNum == 1:
            Comtext = '바위'
            Resulttext = DrawText
        elif ComNum == 2:
            Comtext = '보'
            Resulttext = LoseText
    elif PCNum == 2:
        PCtext = '보'
        if ComNum == 0:
            Comtext = '가위'
            Resulttext = LoseText
        elif ComNum == 1:
            Comtext = '바위'
            Resulttext = WinText
        elif ComNum == 2:
            Comtext = '보'
            Resulttext = DrawText

    return PCtext, Comtext, Resulttext