import random

def shot():
    
    multiple = (0,0,10,10,10,10,10,100,100,100)

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

    sText = '탕! '+shotscore1+'점을 맞췄다. \n 탕! '+shotscore2+'점을 맞췄다. \n 탕! '+shotscore3+'점을 맞췄다. \n 탕! '+shotscore4+'점을 맞췄다. \n 탕! '+shotscore5+'점을 맞췄다.'
    sText2 = '얻은 점수는 '+totalscore+'점!'

    if totalscore >= 2000:
        sText3 = '축하합니다! 1등상 ㅇㅇㅇ를 받았다!'
    elif totalscore < 2000 and totalscore >= 1000 :
        sText3 = '축하합니다! 2등상 '
    elif totalscore < 2000 and totalscore >= 1000 :
        sText3 = '경품 뭐 주냐'
    elif totalscore < 2000 and totalscore >= 1000 :
        sText3 = '경품 뭐 주냐'
    elif totalscore < 2000 and totalscore >= 1000 :
        sText3 = '경품 뭐 주냐'
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
