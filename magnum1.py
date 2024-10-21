import random

hangeuls = ['ㄱ','ㄴ','ㄷ','ㄹ','ㅁ','ㅂ','ㅅ','ㅇ','ㅈ','ㅊ','ㅋ','ㅌ','ㅍ','ㅎ']
colors = ['빨간색','주황색','노란색','연두색','초록색','하늘색','파란색','보라색','자주색','분홍색']

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
    lamb_result = random.randrange(1,101)

    if lamb_result < 51:
        text1 = '이런!'
        text2 = random.choice(['양처럼 생긴 물체가 도망쳤다.','손이 미끄러졌다.'])+' 양털 깎기에 실패했다...'
    
    elif lamb_result > 50 and lamb_result < 99:
        text1 = '양털을 '+str(random.choice(1,41))+'kg 깎았다.'
        text2 = random.choice(colors)+'을 띤 퐁당이를 구출했다!'

    elif lamb_result >= 99:
        colors = colors+['무지개색','오로라빛']
        text1 = '희귀한 '+random.choice(['반짝이','무지개색','오로라빛'])+' 양털을'+str(random.choice(1,51))+'kg 깎았다.'
        text2 = random.choice(colors)+'을 띤 퐁당이를 구출했다!'

    return text1, text2