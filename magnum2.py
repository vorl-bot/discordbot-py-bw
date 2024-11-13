import random

def shot():
    
    multiple = [0,0,10,10,10,10,100,100,100,100]

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

    if totalscore >= 3000:
        sText3 = '축하합니다! 1등상 꽃다발과 사격 퐁당 인형과 5펄을 받았다!'
    elif totalscore < 3000 and totalscore >= 2500 :
        sText3 = '축하합니다! 2등상 꽃 한송이와 퐁당 미니 시계와 4펄을 받았다!'
    elif totalscore < 2500 and totalscore >= 2000 :
        sText3 = '축하합니다! 3등상 퐁당 피규어와 3펄을 받았다!'
    elif totalscore < 2000 and totalscore >= 1500 :
        sText3 = '축하합니다! 4등상 3펄을 받았다!'
    elif totalscore < 1500 and totalscore >= 1000 :
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

def RGBCookingFight():

    



    return

def Kitchen():

    KitchenItem = ['피콕 경 식사예절 포토카드', '안경', '딸기', '카스테라', '피콕 경 취임 기념 주화', 
                   '양털에서 벗어나지 못한 퐁당 "퐁...퐁퐁퐁? 퐁퐁퐁퐁퐁?" (어라...셀라레 배 팔레트 국제 박람회는? 벌써 끝나버린건가?)', '밀면',
                   '요리사 퐁당이 정성을 다해 작은 손으로 휘핑을 돌려 만든 생크림-완제-', '일짱이 되고 싶었던 소의 고기', '돼지고기', '양고기',
                   '혜윰산 쌀', '벨체르산 산양 치즈', '로테폴산 랍스터', '참깨', '튀김가루', '노란색 팽이버섯', '밀가루', '쫄면', '1셀']

    KItem = random.choice(KitchenItem)
    
    return KItem

def Greenhouse():

    GreenhouseItem = ['야자열매', '오이', '가지', '짱돌', '미역', '백년초', '맨드레이크', '두부', '퐁당 피규어', '레몬', '피망', '완두콩',
                      '사과', '옥수수', '양상추', '정원사 퐁당에게 키워주셔서 감사하다는 인사를 드리고 싶었던 토마토', '포도',
                      '정원사 퐁당이 졸고 있을 때 몰래 뜯어 온 로즈마리', '훌쩍이는 퐁당 "퐁퐁포옹… 포포퐁… 포오오오오옹…. (우아앙… 훌쩍… 저는 재료가 아니예요오오….)"', '1셀']

    GItem = random.choice(GreenhouseItem)
    
    return GItem

def Lake():

    LakeItem = ['붓', '장화', '거꾸로 강을 거슬러 올라가고 싶었던 연어(손질됨)', '나이라산 모래', '젤라틴', '호두', '김', '찹쌀가루', '요플레',
                '배', '타조알', '피콕경 동상 미니어처', '참치 뱃살', '광어 지느러미', '공병', '인어옷을 입고 당황한 퐁당 "포, 포옹-퐁퐁퐁퐁..! (자, 잠깐-보지마세욧..!)"',
                '꽃게(손질됨)', '가리비', '장어(손질됨)', '1셀']

    LItem = random.choice(LakeItem)
    
    return LItem

def Seasoning():

    SeasoningItem = ['소금', '설탕', '고춧가루', '간장', '된장', '고추장', '퐁당의 눈물', '피콕 경의 꼬리깃', '까나리액젓', '참기름', '들기름',
                     '치킨스톡', '초콜릿', '커피', '코코아', '꿀', '바닐라 시럽을 머금은 퐁당', '티케산 밀크티', '옹달샘 물', '1셀']

    SItem = random.choice(SeasoningItem)

    return SItem

def Audience():

    ChanceNumber = random.randrange(0,7)
    
    if ChanceNumber >= 0 and ChanceNumber < 3:
        CText = '[당첨!]'
        CText2 = '추가 점수권 획득! 가장 마음에 들었던 요리에 추가 점수를 주세요!'
    elif ChanceNumber == 3:
        CText = '[꽝!]'
        CText2 = '안타깝네요! 친구들에게 애교를 보여주고 옵시다! \n ※해당 미션 완료 시 재 뽑기가 가능합니다.'
    elif ChanceNumber == 4:
        CText = '[꽝!]'
        CText2 = '안타깝네요! 친구들에게 노래를 불러주고 옵시다! \n ※해당 미션 완료 시 재 뽑기가 가능합니다.'
    elif ChanceNumber == 5:
        CText = '[꽝!]'
        CText2 = '안타깝네요! 친구들 앞에서 춤을 추고 옵시다! \n ※해당 미션 완료 시 재 뽑기가 가능합니다.'
    elif ChanceNumber == 6:
        CText = '[꽝!]'
        CText2 = '안타깝네요! 친구들 앞에서 개인기를 하고 옵시다! \n ※해당 미션 완료 시 재 뽑기가 가능합니다.'

    return CText, CText2

def SecretMenu():




    return