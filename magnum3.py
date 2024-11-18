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

    return

def Defence():

    return

def RSP():

    RSPNum = random.randrange(0,101)
    RSPNum = RSPNum % 3

    if RSPNum == 0:
        text = '가위'
    elif RSPNum == 1:
        text = '바위'
    elif RSPNum == 2:
        text = '보'

    return


