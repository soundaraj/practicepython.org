import requests
from bs4 import BeautifulSoup
url = "http://www.vasanthamrecharge.com/aboutus.php"
r = requests.get(url)
soup = BeautifulSoup(r.text)
openfile = open("webpage.txt",'w')
for paragraph in soup.find_all('p'):
    if paragraph.a:
        openfile.write(paragraph.a.text.replace("\n"," ").strip())
    else:
        openfile.write(paragraph.contents[0].encode('utf-8').replace("\n"," ").strip())
openfile.close()
   
