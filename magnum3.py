import random

def spinning():
    spin_result = random.randrange(1,101)

    if spin_result < 51:
        text1 = random.choice(['이런!','앗차!'])
        text2 = random.choice(['섬유가 중간에 끊겨버렸다.','손이 미끄러졌다.'])+' 실 잣기에 실패했다...'
    
    elif spin_result > 50 and spin_result <= 99:
        text1 = random.choice(['야호!','성공!'])
        text2 = '실을 '+str(random.randrange(1,101))+'m만큼 뽑아냈다!'

    return text1, text2

def weaving():
    weave_result = random.randrange(1,101)

    if weave_result < 51:
        text1 = '저가형 옷감이 완성되었다.'
        text2 = '으음... 어찌저찌 성공했지만, 상당히 엉성한 옷감이다. 이걸로 만든 옷을 입고 싶진 않은걸.'

    elif weave_result > 50 and weave_result < 81 :
        text1 = '일반 옷감이 완성되었다.'
        text2 = '무난한 옷감이다. 염색해서 옷을 만들어 입어도 괜찮겠네.'

    elif weave_result > 80 and weave_result < 96 :
        text1 = '고급 옷감이 완성되었다.'
        text2 = '곱고 아름다운 옷감이다. 염색해서 옷을 만들어 입으면 분명 멋질 거야.'

    elif weave_result > 95 :
        text1 = '최고급 옷감이 완성되었다.'
        text2 = '아니, 이건?! 옷감에서 광택이 나는 것만 같다! 염색해서 옷을 만들어 입으면 누구라도 안색이 살 거야!'

    return text1, text2

def valuation():
    value_result = random.randrange(1,101)

    if value_result < 51:
        text = 'D등급'

    elif value_result > 50 and value_result < 71:
        text = 'C등급'

    elif value_result > 70 and value_result < 86:
        text = 'B등급'
    
    elif value_result > 85 and value_result < 96:
        text = 'A등급'

    elif value_result > 95:
        text = 'S등급'

    return text

def Mission():
    
    MissionNum = random.randrange(0,1001)
    MissionNum = MissionNum % 15

    if MissionNum < 2:
        text = '미션 없이 통과! 운이 좋았네.'
    elif MissionNum == 2:
        text = '음악에 맞춰 춤을 추시오.'
    elif MissionNum == 3:
        text = '친구들에게 애교를 보여주시오.'
    elif MissionNum == 4:
        text = '일반 가챠를 1회 뽑으시오.'
    elif MissionNum == 5:
        text = '친구에게 선물을 주시오.'
    elif MissionNum == 6:
        text = '노래방에서 80점 이상을 달성하시오.\n ※실패 시 10분의 제한시간이 지난 후 재도전이 가능합니다.'
    elif MissionNum == 7:
        text = '친구 한 명에게 칭찬을 3개 하시오.'
    elif MissionNum == 8:
        text = '친구에게 가위바위보로 이기시오. \n ※해당 채널에서 !가위바위보 키워드로 이용할 수 있습니다.'
    elif MissionNum == 9:
        text = '의류점에서 물레를 돌리시오.'
    elif MissionNum == 10:
        text = '친구 귀에 "넌 네꺼야" 라고 속삭이시오.'
    elif MissionNum == 11:
        text = '친구 귀에 "난 내꺼야" 라고 속삭이시오.'
    elif MissionNum == 12:
        text = '본인의 비밀 하나를 친구에게 고백하시오.'
    elif MissionNum == 13:
        text = '피콕 경을 칭찬하시오.'
    elif MissionNum == 14:
        text = '퐁당이 성대모사를 하시오.'

    return text

def Aattack():

    ActNum = random.randrange(0,1001)
    ActNum = ActNum % 3

    if ActNum == 0:
        text = '점령전에서 승리했다.'
        ActWinNum = random.randrange(0,100)
        ActWinNum = ActWinNum % 3
        if ActWinNum == 0:
            text2 = '대승리!'
        elif ActWinNum == 1:
            text2 = '안정적 승리!'
        elif ActWinNum == 2:
            text2 = '승리!'
    elif ActNum == 1:
        text = '점령전에서 패배했다.'
        ActLoseNum = random.randrange(0,100)
        ActLoseNum = ActLoseNum % 3
        if ActLoseNum == 0:
            text2 = '아까운 패배!'
        elif ActLoseNum == 1:
            text2 = '패배!'
        elif ActLoseNum == 2:
            text2 = '압도적 패배!'
    elif ActNum == 2:
        text = '점령전에서 패배해 상대팀에게 땅 한 칸을 빼앗겼다.'
        ActLoseNum = random.randrange(0,100)
        ActLoseNum = ActLoseNum % 2
        if ActLoseNum == 0:
            text2 = '패배!'
        elif ActLoseNum == 1:
            text2 = '압도적 패배!'


    return text,text2

def Defence():

    DefNum = random.randrange(0,1001)
    DefNum = DefNum % 3

    if DefNum == 0:
        text = '점령전에서 승리했다.'
        DefWinNum = random.randrange(0,100)
        DefWinNum = DefWinNum % 3
        if DefWinNum == 0:
            text2 = '대승리!'
        elif DefWinNum == 1:
            text2 = '안정적 승리!'
        elif DefWinNum == 2:
            text2 = '승리!'
    elif DefNum == 1:
        text = '점령전에서 패배했다.'
        DefLoseNum = random.randrange(0,100)
        DefLoseNum = DefLoseNum % 3
        if DefLoseNum == 0:
            text2 = '아까운 패배!'
        elif DefLoseNum == 1:
            text2 = '패배!'
        elif DefLoseNum == 2:
            text2 = '압도적 패배!'
    elif DefNum == 2:
        text = '점령전에서 승리해 상대팀에게 땅 한 칸을 빼앗았다.'
        DefWinNum = random.randrange(0,100)
        DefWinNum = DefWinNum % 2
        if DefWinNum == 0:
            text2 = '대승리!'
        elif DefWinNum == 1:
            text2 = '안정적 승리!'

    return text, text2

def Item():

    ItemNum = random.randrange(0,1001)
    ItemNum = ItemNum % 10

    if ItemNum == 0:
        text = '이동횟수 1회 추가권'
        text2 = '기준 시간 내 한 번 더 이동할 수 있습니다.'
    elif ItemNum == 1:
        text = '이동 가능칸 1칸 추가권'
        text2 = '1회 이동 시 한 칸 더 이동할 수 있습니다.'
    elif ItemNum == 2:
        text = '미션패스권'
        text2 = '미션 진행 상태를 수행한 것으로 변경할 수 있습니다.'
    elif ItemNum == 3:
        text = '점령성공권'
        text2 = '무조건 해당 땅을 점령합니다. 상대가 점령방어권을 사용할 경우 다이스 값이 높은 팀이 승리합니다.'
    elif ItemNum == 4:
        text = '점령방어권'
        text2 = '해당 땅에 시도된 점령 시도를 완벽 방어합니다. 상대가 점령성공권을 사용했을 경우 다이스 값이 높은 팀이 승리합니다.'
    elif ItemNum == 5:
        text = '땅 소실'
        text2 = '땅 한 칸을 잃습니다. 자신의 팀이 소유하고 있는 땅 중 잃을 땅 한 칸을 선택하여 흑과 백의 아틀리에 계정을 태그해주세요.'
    elif ItemNum == 6:
        text = '땅 획득'
        text2 = '땅 한 칸을 얻습니다. 자신의 팀이 소유하고 있는 땅과 인접한 땅 중 얻고 싶은 땅 한 칸을 선택하여 흑과 백의 아틀리에 계정을 태그해주세요. 비어있는 땅에만 사용할 수 있습니다.'
    elif ItemNum == 7:
        text = '습격!'
        text2 = '자신의 팀이 소유하고 있는 땅 중 한 칸을 타팀에게 빼앗깁니다. 빼앗길 땅 한 칸과 땅의 새로운 소유주는 운영진 측에서 결정합니다.'
    elif ItemNum == 8:
        text = '침략 성공!'
        text2 = '타팀의 땅 하나를 뺏어올 수 있습니다. 뺏어올 땅 한 칸과 땅의 기존 소유주는 팀은 운영진 측에서 결정합니다.'
    elif ItemNum == 9:
        text = '결과값 교환권'
        text2 = '상대의 결과값과 자신의 결과값을 바꿀 수 있습니다. 공격/방어 키워드 결과값에만 사용 가능합니다.'

    return text, text2


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

def ItemDrop():

    ColNum = random.randrange(0,101)
    ColNum = ColNum % 13
    ColNum = ColNum + 2

    RowNum = random.randrange(0,101)
    RowNum = RowNum % 13

    if RowNum == 0:
        text = 'B'
    elif RowNum == 1:
        text = 'C'
    elif RowNum == 2:
        text = 'D'
    elif RowNum == 3:
        text = 'E'
    elif RowNum == 4:
        text = 'F'
    elif RowNum == 5:
        text = 'G'
    elif RowNum == 6:
        text = 'H'
    elif RowNum == 7:
        text = 'I'
    elif RowNum == 8:
        text = 'J'
    elif RowNum == 9:
        text = 'K'
    elif RowNum == 10:
        text = 'L'
    elif RowNum == 11:
        text = 'M'
    elif RowNum == 12:
        text = 'N'

    text = text + str(ColNum)

    return text







