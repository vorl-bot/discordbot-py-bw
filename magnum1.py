import random

hangeuls = ['ㄱ','ㄴ','ㄷ','ㄹ','ㅁ','ㅂ','ㅅ','ㅇ','ㅈ','ㅊ','ㅋ','ㅌ','ㅍ','ㅎ']

def hyeyum():
    word_result = []
    word = ''
    while len(word_result) < 2:
        hangeul = random.choice(hangeuls)
        newword = list(hangeul)
        word_result = word_result+newword
        word = word+hangeul

    return word


def belcher():
    colors = ['빨간색','주황색','노란색','연두색','초록색','하늘색','파란색','보라색','자주색','분홍색']
    lamb_result = random.randrange(1,101)

    if lamb_result < 51:
        text1 = '이런!'
        text2 = random.choice(['양처럼 생긴 물체가 도망쳤다.','손이 미끄러졌다.'])+' 양털 깎기에 실패했다...'
    
    elif lamb_result > 50 and lamb_result < 99:
        text1 = '양털을 '+str(random.randrange(1,21))+'kg 깎았다.'
        text2 = random.choice(colors)+'을 띤 퐁당이를 구출했다!'

    elif lamb_result >= 99:
        colors = colors+['무지개색','오로라빛']
        text1 = '희귀한 '+random.choice(['반짝이','무지개색','오로라빛'])+' 양털을 '+str(random.randrange(1,21))+'kg 깎았다.'
        text2 = random.choice(colors)+'을 띤 퐁당이를 구출했다!'

    return text1, text2

def rhotepol():
    calcs = ['1','2','3','4','5','6','7','8','9','＋','－','×','÷','√']
    calc_result = random.randrange(1,31)

    if calc_result < 2:
        calc = str(0)
    else:
        calc = random.choice(calcs)
    
    return calc

def transport():
    transNum = random.randrange(1,7)

    if transNum == 1:
        transresult = '중간에 무법자 퐁당이를 만나 물자도 전부 뺏기고 무법자 퐁당이에게도 당해버렸다. 이대로라면 아트라프에 도착할 수 없어….\n 행동불능! '

    elif transNum == 2:
        transresult = '중간에 무법자 퐁당이를 만나 물자를 전부 뺏겼다…. 겨우겨우 아트라프에 도착하긴 했지만… 담당 퐁당이에게 아무 것도 건네줄 수 없었다.\n 의뢰 실패!'

    elif transNum == 3:
        transresult = '중간에 무법자 퐁당이를 만났지만… 해치웠다! 하지만 해치우는데 너무 시간이 걸린 탓일까, 몇몇 무법자 퐁당이는 도망가버렸네…. 물자의 절반이 사라졌다. 아트라프에 도착하긴 했지만… 담당 퐁당이에게 물자의 절반만 건네줄 수 밖에 없었다.\n 의뢰 실패!'
    
    elif transNum == 4:
        transresult = '중간에 무법자 퐁당이를 만나 물자의 절반을 뺏겼다…. 겨우겨우 아트라프에 도착하긴 했지만… 담당 퐁당이에게 물자의 절반만 건네줄 수 밖에 없었다.\n 의뢰 실패!'

    elif transNum == 5:
        transresult = '중간에 무법자 퐁당이를 만났지만… 해치웠다! 무사히 아트라프에 도착해 담당 퐁당이에게 물자를 전부 건네주었다.\n 의뢰 성공!'

    elif transNum == 6:
        transresult = '무법자 퐁당이를 만나지 않고 무사히 아트라프에 도착했다. 담당 퐁당이에게 물자를 전부 건네주었다.\n 의뢰 성공!'

    return transresult