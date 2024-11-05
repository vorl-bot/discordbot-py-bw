import random

def soriziller():

    songscore = random.randrange(0,100)

    Text=""
    Text=Text+str(songscore)
    Text=Text+"점!"

    if songscore == 100:
        Text2 = '환상적인 목소리! 당신이~ 👍***짱***이랍니다~'
    elif songscore <=99 and songscore >= 95:
        Text2 = '노래를 너~어무 잘불러서 딩동퐁당 ***기절!***🤩'
    elif songscore <=94 and songscore >=90:
        Text2 = '한곡 더~ 듣고 싶은 실력! **불↘러→줄↘꺼↗죠↗??**🎤'
    elif songscore <= 89 and songscore >= 85:
        Text2 = '이렇게 잘 부를수가?!😃 매~력이~ 넘쳐요~'
    elif songscore <=84 and songscore >=80:
        Text2 = '딩동퐁당 완~전 **두근!** 🥰정말 멋져요~~'
    elif songscore <=79 and songscore>=70:
        Text2 = '목소리에~ 매력이 철철~ 하트💚하트💙~'
    elif songscore <=69 and songscore>=60:
        Text2='지금 딱 좋아요!!😉 그 느낌으로 한! 곡! 더!!'
    elif songscore<=59 and songscore>=50:
        Text2='점수는 점수일 뿐. 즐거우면 100점이죠~😌'
    elif songscore <=49 and songscore>=10:
        Text2='너~~어 노래에 조금만 더 ***집!중!*** 🙁'
    elif songscore<=9 and songscore>=0:
        Text2='이 점수! 어쩌면 좋지? 진짜 모르게쒀요오~ 😯'


    return Text, Text2

