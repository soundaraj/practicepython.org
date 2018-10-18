import requests
from bs4 import BeautifulSoup
url = 'https://www.vanityfair.com/style/society/2014/06/monica-lewinsky-humiliation-culture'
r = requests.get(url)
soup = BeautifulSoup(r.text)
with open("demo.txt",'w') as openfile:
    
    for article in soup.find_all(class_="content-section"):
        openfile.write(article.encode('utf-8').strip())
        #print(article.text)
    openfile.close()
