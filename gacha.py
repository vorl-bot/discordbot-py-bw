import random
items = ['벼루','마법소녀 피규어','무료 식권','해시계','달토끼 인형',
         '나비 향갑 노리개','은행잎','알록달록한 구슬','기러기 인형',
         '반짝반짝한 유리병','미니 카메라','직소퍼즐','강아지 인형',
         '교환 일기','해파리 키링','양 인형','나사세트','꽃과 춤의 축제 팜플렛',
         '나비 머리 핀','모래 시계','별 모양 귀걸이','버섯 키링',
         '1개 더! 가 적힌 아이스크림 막대','선글라스','청색 두루마기',
         '꽃무늬 원형 거울','동그란 과일 사탕 교환권','가죽 팔찌','씨앗 주머니',
         '해파리 인형','채워지지 않은 앨범','양갈래 머리 인형','말 안장',
         '우정룩(세트 잠옷 2벌)','바다 무드등','나뭇가지','두유 교환권',
         '구급상자','소리나는 장식이 달린 팔찌','공연 팜플렛',
         '음표 모양 열쇠고리','점보 특대 사이즈 컵라면 (10인분) 교환권',
         '스프링 줄 노트','목조 사막여우 반가면','분홍색 가루의 모래시계',
         '부러진 목검','조향 노트','동물의 뼈','가죽 공예 키트','색색의 꽃다발',
         '미니 슬레이트(베이지)','입체 퍼즐','터그 놀이 로프 장난감',
         '정말 맛있는 심해 괴식 요리 3선 식사권','조개가 든 유리병',
         '요거트 교환권','절연 테이프','〈해바라기와 여름 청년〉 악보',
         '색만 다르고 꼭 닮은 여자아이 두 명이 찍힌 사진','배 모형 부품']

specialA = [['『벨체르 전통 복식A』','https://img1.daumcdn.net/thumb/R1280x0/?scode=mtistory2&fname=https%3A%2F%2Fblog.kakaocdn.net%2Fdn%2Fr6EcN%2FbtsKkwgnICY%2FZsafMAYbaK4C309lVyRG6K%2Fimg.png',''],
            ['『벨체르 전통 복식B』','https://img1.daumcdn.net/thumb/R1280x0/?scode=mtistory2&fname=https%3A%2F%2Fblog.kakaocdn.net%2Fdn%2FyiTZz%2FbtsKkdn4RJR%2FuF2JKugGFNZivyeJen0Rq0%2Fimg.png',''],
            ['『잠옷』','https://img1.daumcdn.net/thumb/R1280x0/?scode=mtistory2&fname=https%3A%2F%2Fblog.kakaocdn.net%2Fdn%2FA0V8N%2FbtsKkb4Oyw1%2FvUOJw9FKsmPqpZNH8ioAO1%2Fimg.png',''],
            ['『퐁당 잠옷』','https://img1.daumcdn.net/thumb/R1280x0/?scode=mtistory2&fname=https%3A%2F%2Fblog.kakaocdn.net%2Fdn%2FcyeGdn%2FbtsKkYKnKSB%2FbyVdJ22kCmVKZ5Q6DMwvnk%2Fimg.png',''],
            ['『피콕 경 잠옷』','https://img1.daumcdn.net/thumb/R1280x0/?scode=mtistory2&fname=https%3A%2F%2Fblog.kakaocdn.net%2Fdn%2FPN0O2%2FbtsKkcQdm0E%2FHqHMJKesUpiH1JKEJKwH6k%2Fimg.png',''],
            ['『셀라레 아카데미 체육복A』','https://img1.daumcdn.net/thumb/R1280x0/?scode=mtistory2&fname=https%3A%2F%2Fblog.kakaocdn.net%2Fdn%2F5EKwq%2FbtsKk267Hdc%2Fx7G66UkxkHT4K6e6pwu7TK%2Fimg.png',''],
            ['『셀라레 아카데미 체육복B』','https://img1.daumcdn.net/thumb/R1280x0/?scode=mtistory2&fname=https%3A%2F%2Fblog.kakaocdn.net%2Fdn%2F6ZBEV%2FbtsKlwNqHfv%2F8qdntiBKkTbpyCQl1elRDk%2Fimg.png','']]

specialB = [['『빛의 종소리 퐁당이 인형(10cm)』','어쩐지 건방진 표정을 하고 있는 퐁당이 인형. 별 모양의 머리 장식이 인상적이다.']]

specialC = ['퐁당이 인형(10cm)','퐁당이 인형(20cm)','피콕 경 인형','퐁당이 모자','피콕 경 모자','피콕 경 포토카드 세트','퐁당이 포토카드 세트','퐁당이 특제 음료수 교환권','만화책 대여권']


def getGacha():
    item = random.choice(items)

    return item

def specialGacha():
    specialNum = random.randrange(1,101)

    if specialNum < 21:
        special = random.choice(specialA)

    elif specialNum > 20 and specialNum < 51:
        special = random.choice(specialB)

    else:
        special = random.choice(specialC)


    return special