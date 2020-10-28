import requests
from bs4 import BeautifulSoup


url = 'https://overreacted.io/'
page = requests.get(url)

heading=[]
links=[]
if page.status_code == 200:
    soup = BeautifulSoup(page.content, 'html.parser')
    head = soup.select( 'h3 a')
    for title in head:
        heading.append(title.text)
print(heading)

for link in soup.find_all('a', href=True):
    links.append(link['href'])
del links[:2]
del links[29:]

print(links)
with open('Primer/txt2.txt', 'w' , encoding='utf-8') as file:
    for i in range(len(links)):
        file.write("{a} - https://overreacted.io{b}\n".format(a=heading[i],b=links[i]))


