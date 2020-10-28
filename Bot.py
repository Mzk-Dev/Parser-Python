import datetime , sys
Spisok=[]
shet=[]
def create():
    while True :
        a=str(input('Add name :'))
        b=0
        c=str(input('Add description :'))
        d=str(datetime.datetime.now())
        e=0
        if a!=False and c!=False :
            return Spisok.extend([[a,b,c,d,e]]),shet.append('a')
        else :
            continue

def read() :
    a=int(input('Enter task number :'))
    return print(str(Spisok[a][0:6]))

def update() :
    while True:
        a=int(input('Enter tusk number :'))
        #if a is float or str :
           # a=int(input('PLS enter numeral :'))
        print(Spisok[a])
        b=int(input('What kind of replacement? Enter index :'))
        #if b is float or str :
            #b=int(input('PLS enter numeral :'))
        c=str(input('Change to :'))
        return Spisok[a][b]==c

def delete():
    print(Spisok)
    a=int(input('What do you want to delete :'))
    if a is str or float :
        a=int(input('PLS enter numeral'))
    print(Spisok[a])
    b=int(input(f'Again (if u want delete all {Spisok[a]} - enter (-10)'))#???????????//
    if b == (-10) :
        del (Spisok[a])
        return print("deleted")
    if b is str or float :
        b=int(input('PLS enter numeral'))
    del Spisok[a][b]
    return print('deleted')


def done():
    print(Spisok)
    a=int(input('What task is completed? :'))
    #if a is str or float :
        #a=int(input('PLS enter numeral'))
    return Spisok[a][1]==1,Spisok[a][4]==datetime.datetime.now()#????????????????

def list() :
    for i in str(len(shet)):
        print(str(Spisok[i]))

def save():
     with open( 'txt1.txt' , 'w', encoding="utf8") as file:
         file.write(str(Spisok))
         return print('ok')


command=['create','read','update','delete','done','list','save','exit']
while True :
    print(command)
    vvod=int(input('Choice command 1-8:'))
    a=command[vvod-1]
    print(a)
   # function=dict(1 : create , 2 : read, 3 : update , 4:delete, 5:done,6:list ,7:save,8:exit)
   # function[vvod]()
    if vvod==1 :
        create()
    if vvod==2:
        read()
    if vvod==3:
        update()
    if vvod==4:
        delete()
    if vvod==5 :
        done()
    if vvod==6:
        list()
    if vvod==7 :
        save()
    if vvod==8:
        exit()

