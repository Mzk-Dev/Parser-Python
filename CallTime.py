import math
import sys
import collections


calls=collections.defaultdict(list)
calls1=[]

for filename in sys.argv[1:] :
    with open (filename, 'r',encoding= 'utf8') as file :
        for line in file:
            line = line.strip().split()
            calls1+=[line]
            calls[line[0]].append(math.ceil(int(line[-1])/60))

def price(s):
	if s <=100:
		p = s*1
	else:
		p = 100 + ((s-100)*2)
	return p

for key, value in calls.items():
    calls[key]=price(sum(value))
    print(('Стоимость звонков за {0} составляет - {1} монет'.format(key, calls[key])))




