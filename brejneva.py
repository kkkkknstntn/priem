import pandas as pd
import xlsxwriter
import re


def remove_leading_zeros(s):
    return re.sub(r'^0+', '', s)

# Путь к вашему файлу Excel
file_path = 'kniit.xlsx'

# Чтение данных из файла Excel
df = pd.read_excel(file_path)
from collections import OrderedDict

# Выбор диапазона ячеек от A до AH
selected_cells = df.iloc[:, :35]  # Предполагается, что у вас есть 10 столбцов от A до J
selected_cells = selected_cells[2:]
# Преобразование выбранного диапазона в список
cell_list = selected_cells.values.tolist()

# print(cell_list)


class Abitura:
    def __init__(self, row=[], prior=[], tables=[], dop=[]):
        self.row = row
        self.prior = prior
        self.tables = tables
        self.dop = dop


kniit = {
        "Информатика и вычислительная техника": "ИВТ",
        "Математическое обеспечение и администрирование информационных систем": "МОАИС",
        "Программная инженерия": "ПИ",
        "Компьютерная безопасность": "КБ",
        "Фундаментальная информатика и информационные технологии": "ФИИТ",
        "Системный анализ и управление": "САУ"

    }

workbook = xlsxwriter.Workbook('kniit2.xlsx')
worksheet = workbook.add_worksheet()

abituras_old = {}
abituras_old["budj_obs"] = OrderedDict()
abituras_old["budj_osob"] = OrderedDict()
abituras_old["cel"] = OrderedDict()
abituras_old["kom"] = OrderedDict()
abituras_old["zo"] = OrderedDict()
import csv

for fl in abituras_old:
    with open("old/" + fl + ".csv", mode='r') as file:
        reader = csv.reader(file)
        for row in reader:
            row1 = row[0].split(';')
            abituras_old[fl][row1[0]] = row1
h = 0
abituras_arr=[]
abituras = {}

for row in cell_list:
    row[12] = row[12].split('_')[2:]
    if row[12][-1][:3] in ["Бак", "Спе"]:
        if not isinstance(row[6],str):
            row[6] = remove_leading_zeros(str(row[5]))
        zam =''
        lich = "лично"
        if row[21] == "Нет документа об образовании":
            zam = row[21]
        if row[31] != "Лично":
            lich = "госуслуги"
        row_ab = [row[4],row[6],'',row[32],'','',lich, zam]
        print(row_ab)
        abituras[row[6]] = Abitura()
        # abituras[remove_leading_zeros(row[6])]
    # print(row)
    if row[12][-1][:3] in ["Бак","Спе"] and row[6] not in abituras_arr :
        abituras_arr.append(row[6])
        flag = False
        for fl in abituras_old:

            if row[6] in abituras_old[fl]:
                if abituras_old[fl][row[6]][1] != '':
                    flag = True
        if not flag:
            worksheet.write(h, 1, row[4])
            worksheet.write(h, 4, row[33])
            h += 1

workbook.close()
