import csv

groups = {}

zao = {
    '0': "очная",
    '1': "очно-заочная",
    '2': "заочная"
}

with open("ssu_abit_groups.csv", mode='r') as file:
    reader = csv.reader(file)
    for row in reader:
        groups[row[0]] = row

with open("ssu_abit_specs.csv", mode='r') as file:
    reader = csv.reader(file)
    for row in reader:
        groups[row[1]] += [row[2]]


fin = []
i = 0
with open("ssu_abit_spisok_with_points.csv", mode='r') as file:
    reader = csv.reader(file)
    for row in reader:
        if i > 0:
            group = groups[row[1]]
            lvl = int(group[4])
            if lvl < 4 or lvl == 5:
                fourth = row[1] + "_" + group[2] + "_" + group[3] + "/" + group[5] + "_" + zao[group[6]] + "_" + group[
                    -1]
                new_row = [row[6], row[7], row[1], row[9], fourth, row[5]] + row[-1].split('.')
                print(new_row)
                fin.append(new_row)
        i += 1

with open("student1.csv", 'a', newline='') as csvfile:
    writer = csv.writer(csvfile)
    for row in fin:
        writer.writerow(row)
