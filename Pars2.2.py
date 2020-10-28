import requests
from bs4 import BeautifulSoup


url = 'https://flaviocopes.com/'
page = requests.get(url)
text=[]
heading=[]
links=[]
if page.status_code == 200:
    soup = BeautifulSoup(page.content, 'html.parser')
    head = soup.select( 'a h4')
    for title in head:
        heading.append(title.text)
print(heading)


for link in soup.find_all('a', href=True):
    if len(link['href'])>25:
        links.append(link['href'])
#print(len(heading))
del links[100:]
#print(len(links))
print(links)

i=0
with open('txt3.txt', 'w', encoding='utf-8') as file:
    while i<100 :
        a=[]
        url='{0}'.format(links[i])
        page = requests.get(url)
        soup = BeautifulSoup(page.content, 'html.parser')
        text1 = soup.find('div').find_all('p')
        a.append(text1)
        file.write("{q} - \n{b}\n".format(q=heading[i], b=a))
        i+=1
#print(text)

