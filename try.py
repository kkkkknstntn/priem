import requests
from bs4 import BeautifulSoup
import re

st_accept = "text/html"
st_useragent = "Mozilla/5.0 (Macintosh; Intel Mac OS X 12_3_1) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/15.4 Safari/605.1.15"
headers = {
    "Accept": st_accept,
    "User-Agent": st_useragent
}

url = "https://www.sgu.ru/svodka/1296"
req = requests.get(url)
src = req.text
soup = BeautifulSoup(src, 'lxml')
title = soup.find_all(class_="svodka-table__info-wrap")[0]
s = title.find_all(class_="svodka-table__info-name")
print(s[2].string, s[4].string, s[5].string)

