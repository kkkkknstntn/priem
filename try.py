import requests
from bs4 import BeautifulSoup
import re

st_accept = "text/html"
st_useragent = "Mozilla/5.0 (Macintosh; Intel Mac OS X 12_3_1) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/15.4 Safari/605.1.15"
headers = {
    "Accept": st_accept,
    "User-Agent": st_useragent
}

url = "https://www.sgu.ru/svodka/1295"
req = requests.get(url)
src = req.text
soup = BeautifulSoup(src, 'lxml')
tables = soup.find_all('table')
# print(tables)
for index, table in enumerate(tables):
    for row in table.find_all('tr'):
        cols = row.find_all('td')
        cols = [col.text.strip() for col in cols]
        # print(cols)
        if len(cols) > 0:
            cols[10] = ' '.join(cols[10].split())[4:]
            cols[9] = int(cols[9])
            s = cols[10].split()
            print(s)