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

def TLmission():

    return

def TLitem():

    return

def TLattack():

    return

def TLdefence():

    return