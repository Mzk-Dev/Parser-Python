import random
import sys
poem=["her",'his','the','a','another']
poem1=['cat','dog','men','woman','boy','girl']
poem2=['sang','run','jumped','hoped']
poem3=['loudly','quietly','well','badly']
q=0#Счетчик
r=0
try:
    while True :
        e=int(sys.argv[1])
        if 0<e>10:
            e==q
        else :
            q=None
        choice=random.randint(0,1)
        if q==5 or r==e  :
            break
        a=random.choice(poem)
        b=random.choice(poem1)
        c=random.choice(poem2)
        if choice == 1 :
            d=random.choice(poem3)
        else :
            d=None
        if d is not None :
            print(a,b,c,d)
        else :
            print(a,b,c)
        if q is not None:
            q+=1
        r+=1

except ValueError or IndexError:
    q=0
    while True :
        choice=random.randint(0,1)
        if q==5 :
            break
        a=random.choice(poem)
        b=random.choice(poem1)
        c=random.choice(poem2)
        if choice == 1 :
            d=random.choice(poem3)
        else :
            d=None
        if d is not None :
            print(a,b,c,d)
        else :
            print(a,b,c)
        q+=1

