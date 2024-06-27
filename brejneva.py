import pandas as pd

# Путь к вашему файлу Excel
file_path = 'kniit.xlsx'

# Чтение данных из файла Excel
df = pd.read_excel(file_path)

# Выбор диапазона ячеек от A до AH
selected_cells = df.iloc[:, :35]  # Предполагается, что у вас есть 10 столбцов от A до J
selected_cells = selected_cells[2:]
# Преобразование выбранного диапазона в список
cell_list = selected_cells.values.tolist()
for row in cell_list:
    print(row)
# print(cell_list)