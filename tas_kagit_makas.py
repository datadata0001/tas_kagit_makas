import random
score = 0
pc_score = 0
options = ['tas','kagit','makas']

while True:
    
    user_play =input('tas/kagit/makas ya da q ile cikis: ').lower()
    if user_play == 'q':
        break
    if user_play not in options:
        continue
    random_value = random.randint(0,2)
    pc_play = options[random_value]
    print(pc_play)

    if user_play == 'tas' and pc_play == 'makas':
        print("Kazandin!")
        score+=1
    elif user_play == 'kagit' and pc_play == 'tas':
        print("Kazandin!")
        score+=1
    elif user_play == 'makas' and pc_play == 'kagit':
        print("Kazandin!")
        score+=1
    elif user_play == pc_play:
        print('Berabere')
        breakpoint
    elif pc_score == 3:
        ('Bilgisayar 3 defa kazanmis oldu!')
    elif score == 3:
        ('3 Defa kazanmis oldun!')
    else:
        print("Bilgisayar Kazandi!")
        pc_score+=1
   
        
        
    
        
print('Tebrikler', score ,'defa kazandin!')
print('Bilgisayar', pc_score , 'defa kazandi!')
print('GULE GULE <3 <3 <3')   
    

