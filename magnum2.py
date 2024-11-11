import random

def shot():
    

    return

def yoyotsuri():

    yoyocolors =['맑은 하늘', '주홍 하늘', '밤하늘','내 퍼스널 컬러','알록달록 꽃','피콕','퐁당']
    yoyonum = random.randrange(1,101)

    if yoyonum > 0 and yoyonum <= 51:
        Text = random.choice['풍덩!','앗차!']
        Text2 = random.choice['물풍선이 다시 풀에 빠져버렸어~. 아쉬워라.', '종이 낚시끈이 물에 젖어버렸다. 이러면 건질 수가 없어!']
    elif yoyonum >= 50 and yoyonum <= 101:
        Text = random.choice(yoyocolors)+'물풍선을 건졌다.'
        Text2 = '고무줄 고리에 손을 넣어 튕겨 놀아볼까?'

    return Text, Text2
