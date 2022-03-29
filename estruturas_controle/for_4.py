from random import randint

def draw_num(): return randint(1, 6)

for i in range(1, 7):
    if i % 2: continue
    if i == draw_num():
        print('Acertou', i)
        break # O brake tambem escapa do else ligado ao for
    
else: print('Nao acertou!')
    