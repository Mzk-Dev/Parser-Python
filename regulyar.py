import re
list=[]
while True:
    Vvod=input('Enter 1 number')
    if not Vvod :
        break
    else:
        list.append(Vvod)
number=re.compile(r'''[\(]?\d{3}[\)]?-? ?d{3}-? ?\d{4}''')
matches=[]
for match in number.findall(list):
    matches.append(match)
print(matches)


