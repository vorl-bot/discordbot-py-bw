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
    weave_result = 