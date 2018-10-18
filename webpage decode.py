import requests
from bs4 import BeautifulSoup
url = 'http://www.vasanthamrecharge.com/aboutus.php'
r = requests.get(url)
soup = BeautifulSoup(r.text)
for title in soup.find_all("h2"):
    print(title.text)
