import random

def shot():
    
    multiple = [0,0,10,10,10,10,10,100,100,100]

    shotscore1 = random.randrange(0,1001)
    shotscore1 = shotscore1 % 11
    shotscore1 = shotscore1 * int(random.choice(multiple))

    shotscore2 = random.randrange(0,1001)
    shotscore2 = shotscore2 % 11
    shotscore2 = shotscore2 * int(random.choice(multiple))

    shotscore3 = random.randrange(0,1001)
    shotscore3 = shotscore3 % 11
    shotscore3 = shotscore3 * int(random.choice(multiple))

    shotscore4 = random.randrange(0,1001)
    shotscore4 = shotscore4 % 11
    shotscore4 = shotscore4 * int(random.choice(multiple))

    shotscore5 = random.randrange(0,1001)
    shotscore5 = shotscore5 % 11
    shotscore5 = shotscore5 * int(random.choice(multiple))
    
    totalscore = shotscore1+shotscore2+shotscore3+shotscore4+shotscore5

    sText = '탕! '+str(shotscore1)+'점을 맞췄다. \n 탕! '+str(shotscore2)+'점을 맞췄다. \n 탕! '+str(shotscore3)+'점을 맞췄다. \n 탕! '+str(shotscore4)+'점을 맞췄다. \n 탕! '+str(shotscore5)+'점을 맞췄다.'
    sText2 = '얻은 점수는 '+str(totalscore)+'점!'

    if totalscore >= 3500:
        sText3 = '축하합니다! 1등상 꽃다발과 사격 퐁당 인형과 5펄을 받았다!'
    elif totalscore < 3500 and totalscore >= 3000 :
        sText3 = '축하합니다! 2등상 꽃 한송이와 퐁당 미니 시계와 4펄을 받았다!'
    elif totalscore < 3000 and totalscore >= 2500 :
        sText3 = '축하합니다! 3등상 퐁당 피규어와 3펄을 받았다!'
    elif totalscore < 2500 and totalscore >= 2000 :
        sText3 = '축하합니다! 4등상 3펄을 받았다!'
    elif totalscore < 2000 and totalscore >= 1000 :
        sText3 = '축하합니다! 5등상 1펄을 받았다!'
    elif totalscore >=0 and totalscore < 1000:
        sText3 = '참가상 1셀을 받았다!'

    return sText, sText2, sText3

def yoyotsuri():

    yoyocolors =['맑은 하늘', '주홍 하늘', '밤하늘','내 퍼스널 컬러','알록달록 꽃','피콕','퐁당']
    yoyonum = random.randrange(1,101)

    if yoyonum > 0 and yoyonum <= 51:
        Text = random.choice(['풍덩!','앗차!'])
        Text2 = random.choice(['물풍선이 다시 풀에 빠져버렸어~. 아쉬워라.', '종이 낚시끈이 물에 젖어버렸다. 이러면 건질 수가 없어!'])
    elif yoyonum >= 50 and yoyonum < 101:
        Text = random.choice(yoyocolors)+' 물풍선을 건졌다.'
        Text2 = '고무줄 고리에 손을 넣어 튕겨 놀아볼까?'

    return Text, Text2
