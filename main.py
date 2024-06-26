import requests
from bs4 import BeautifulSoup
import re
import csv

st_accept = "text/html"
st_useragent = "Mozilla/5.0 (Macintosh; Intel Mac OS X 12_3_1) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/15.4 Safari/605.1.15"
headers = {
    "Accept": st_accept,
    "User-Agent": st_useragent
}





urls = ["https://www.sgu.ru/svodka/1295", "https://www.sgu.ru/svodka/1494", "https://www.sgu.ru/svodka/1619",
        "https://www.sgu.ru/svodka/1787",
        "https://www.sgu.ru/svodka/1353", "https://www.sgu.ru/svodka/2404", "https://www.sgu.ru/svodka/1294",
        "https://www.sgu.ru/svodka/1495", "https://www.sgu.ru/svodka/1620", "https://www.sgu.ru/svodka/1788",
        "https://www.sgu.ru/svodka/1354", "https://www.sgu.ru/svodka/2396", "https://www.sgu.ru/svodka/2397",
        "https://www.sgu.ru/svodka/1293", "https://www.sgu.ru/svodka/1496", "https://www.sgu.ru/svodka/1621",
        "https://www.sgu.ru/svodka/1791",
        "https://www.sgu.ru/svodka/1355", "https://www.sgu.ru/svodka/2402", "https://www.sgu.ru/svodka/1292",
        "https://www.sgu.ru/svodka/1497", "https://www.sgu.ru/svodka/1622", "https://www.sgu.ru/svodka/1792",
        "https://www.sgu.ru/svodka/1356", "https://www.sgu.ru/svodka/2398",
        "https://www.sgu.ru/svodka/2399", "https://www.sgu.ru/svodka/1436", "https://www.sgu.ru/svodka/1500",
        "https://www.sgu.ru/svodka/1625", "https://www.sgu.ru/svodka/1795", "https://www.sgu.ru/svodka/1437",
        "https://www.sgu.ru/svodka/1291","https://www.sgu.ru/svodka/1624","https://www.sgu.ru/svodka/1794",
        "https://www.sgu.ru/svodka/1358","https://www.sgu.ru/svodka/2413","https://www.sgu.ru/svodka/2414","https://www.sgu.ru/svodka/2415",
        "https://www.sgu.ru/svodka/1296","https://www.sgu.ru/svodka/1498","https://www.sgu.ru/svodka/1623","https://www.sgu.ru/svodka/1793",
        "https://www.sgu.ru/svodka/1357"
        # ,"https://www.sgu.ru/svodka/1499"
        ]

kniit = {
    "Информатика и вычислительная техника": "ИВТ",
    "Математическое обеспечение и администрирование информационных систем": "МОАИС",
    "Программная инженерия": "ПИ",
    "Компьютерная безопасность": "КБ",
    "Фундаментальная информатика и информационные технологии": "ФИИТ",
    "Системный анализ и управление": "САУ"

}


not_kniit={
    "Бизнес-информатика": "БИ",
    "Информационные системы и технологии": "ИСТ",
    "Прикладная математика и информатика": "ПМИ",
    "Математика и компьютерные науки": "МКН",
    "Прикладная информатика социологии": "ПРИ соц",
    "Прикладная информатика экономике": "ПРИ экон мех",
    "Прикладная информатика": "ПРИ мех",
    "Конструирование и технология электронных средств": "КТЭС",
    "Биотехнические системы и технологии": "БСТ",
    "Техносферная безопасность": "ТБ",
    "Геология": "Геол",
    "Механика и математическое моделирование": "МиММ",
    "Электроника и наноэлектроника": "ЭиН",
    "Экономика": "Экон",
    "Таможенное дело": "Тамож",
    "Менеджмент": "Менедж",
    "Медицинская биофизика": "МБ",
    "Медицинская кибернетика": "МК",
    "Прикладная геология": "ПГ",
    "Инфокоммуникационные технологии и системы связи": "ИТиСС",
    "Педагогическое образование Информатика": "ПО инф",
    "Педагогическое образование Математическое": "ПО мат",
    "Психолого-педагогическое образование": "ППО",
    "Социология": "Соц",
    "Сервис": "Серв"
}



class Abitura:
    def __init__(self, row, prior, osoboe, tables, num,dop):
        self.row = row
        self.prior = prior
        self.osoboe = osoboe
        self.tables = tables
        self.num = num
        self.dop = dop


abituras = {}

pattern = r"\d{1,3}\.\d{1,3}\.\d{1,3}"
pattern2 = r'(Бюджет/Общие|Бюджет/Особое|Бюджет/Отдельная|Полное|Целевой)'

for url in urls:
    req = requests.get(url)
    src = req.text
    soup = BeautifulSoup(src, 'lxml')
    tables = soup.find_all('table')
    with open('example.txt', 'a', encoding='utf-8') as file:
        for index, table in enumerate(tables):
            for row in table.find_all('tr'):
                cols = row.find_all('td')
                cols = [col.text.strip() for col in cols]
                if len(cols) > 0:
                    if cols[1] not in abituras:
                        # print(url, cols)
                        # print(url, cols[1])
                        cols[10] = ' '.join(cols[10].split())[4:]
                        cols[9] = int(cols[9])
                        pr = -1
                        i = 0
                        prior = [""] * 6
                        dop=[]
                        osoboe = [""] * 6
                        tables = set()
                        s = cols[10].split()
                        print(url)

                        ttl = soup.find_all(class_="svodka-table__info-wrap")[0]
                        ttl = ttl.find_all(class_="svodka-table__info-name")

                        ttl = (ttl[2].string, ttl[4].string, ttl[5].string.split(' ')[0])
                        while cols[9] >= len(prior):
                            prior.append('')
                            osoboe.append('')

                        prior[cols[9]-1] = kniit[ttl[0]]

                        if ttl[1] == "Заочная":
                            prior[cols[9]-1] = "ПИ ЗО"
                            tables.add("zo")
                        if ttl[2] == "Бюджет/Общие":
                            tables.add("budj_obs")
                        if ttl[2] == "Бюджет/Особое":
                            tables.add("budj_osob")
                            osoboe[cols[9]-1] += "ОП "
                        if ttl[2]== "Бюджет/Отдельная":
                            tables.add("budj_otdel")
                            osoboe[cols[9]-1] += "ОК "
                        if ttl[2] == "Полное":
                            tables.add("kom")
                            osoboe[cols[9]-1] += "К "

                        if ttl[2] == "Целевой":
                            tables.add("cel")
                            osoboe[cols[9]-1] += "Ц "

                        while i < len(s):
                            if re.match(pattern, s[i]) is not None:
                                pr += 1
                                if pr == cols[9] - 1:
                                    pr += 1
                                if pr > 4:
                                    prior.append('')
                                    osoboe.append('')
                                name = ""
                                j = i + 1
                                flag = True
                                while re.match(pattern2, s[j]) is None:
                                    if s[j] == "(Профиль:":
                                        flag = False
                                        print(name, "Прикладная информатика" in name or "Педагогическое образование" in name)
                                        if "Прикладная информатика" in name:
                                            name += " " + s[j + 4]
                                            print(name)
                                        if "Педагогическое образование" in name:
                                            name += " " + s[j + 1]
                                            print(name)

                                    if flag:
                                        name += " " + s[j]
                                    j += 1
                                name = name[1:]

                                if name in kniit:
                                    prior[pr] = kniit[name]
                                    if s[j] == "Бюджет/Общие":
                                        tables.add("budj_obs")
                                        if s[j + 2] == "(заоч.)":
                                                prior[pr] = "ПИ ЗО"
                                        tables.add("zo")
                                        osoboe[pr] = ""

                                    elif s[j] == "Бюджет/Особое":
                                        tables.add("budj_osob")
                                        if s[j + 2] == "(заоч.)":
                                            prior[pr] = "ПИ ЗО"
                                            tables.add("zo")
                                        osoboe[pr] = "ОП "
                                    elif s[j] == "Бюджет/Отдельная":
                                        tables.add("budj_otdel")
                                        if s[j + 2] == "(заоч.)":
                                            prior[pr] = "ПИ ЗО"
                                            tables.add("zo")
                                        osoboe[pr] = "ОК "
                                    elif s[j] == "Полное":
                                        tables.add("kom")
                                        osoboe[pr] = "К "
                                        if s[j + 3] == "(заоч.)":
                                            prior[pr] = "ПИ ЗО"
                                            tables.add("zo")

                                    elif s[j] == "Целевой":
                                        tables.add("cel")
                                        if s[j + 2] == "(заоч.)":
                                            tables.add("zo")
                                            prior[pr] = "ПИ ЗО"
                                        osoboe[pr] = "Ц "
                                else:
                                    if name in not_kniit:
                                        dop.append(not_kniit[name])
                                    else:
                                        # print(name)
                                        dop.append(name)
                                    if s[j] == "Бюджет/Общие":
                                        if s[j + 2] == "(заоч.)":
                                               dop.append(" ЗО")

                                    elif s[j] == "Бюджет/Особое":

                                        if s[j + 2] == "(заоч.)":
                                            dop.append(name+ " ЗО")
                                        dop[-1]+=" ОП"
                                    elif s[j] == "Бюджет/Отдельная":

                                        if s[j + 2] == "(заоч.)":
                                            dop.append(" ЗО")
                                        dop[-1] += " ОК"
                                    elif s[j] == "Полное":

                                        if s[j + 2] == "затрат":
                                            if s[j + 3] == "(заоч.)":
                                                dop.append(" ЗО")
                                            dop[-1] += " К"
                                        else:
                                            if s[j + 5] == "(заоч.)":
                                                dop.append(" ЗО")
                                            dop[-1] += " КИ"
                                    elif s[j] == "Целевой":
                                        if s[j + 2] == "(заоч.)":
                                            dop.append(" ЗО")
                                        dop[-1] += " Ц"
                                # print(dop)
                                i = j
                            i += 1

                        if "ПИ ЗО" in prior or "ПИ ЗО" in dop:
                            tables.add("zo")
                        for h in range((len(prior))):
                            prior[h] = prior[h] + " " + osoboe[h]

                        abituras[cols[1]] = Abitura(cols[1:8], prior, osoboe, tables, cols[9] - 1, dop)
                        file.write(str(cols) + '\n')

for ab in abituras:
    row = abituras[ab].row
    for i in range(len(row)):
        if row[i] == 'Нет данных' or row[i] == '---':
            row[i] = ''
        elif row[i] == 'Ориг.':
            row[i] = 'Оригинал'

    for file in abituras[ab].tables:
        filename = file+".csv"
        new_row = row[0:1]+['']+row[1:6]+abituras[ab].prior[0:5]+[' '.join(abituras[ab].prior[5:])+ " " + ' '.join(abituras[ab].dop)]+[row[6]]
        with open(filename, 'a', newline='') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(new_row)

    print(new_row)
    # print(abituras[ab].row, abituras[ab].prior)

