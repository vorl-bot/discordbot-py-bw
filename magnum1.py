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
