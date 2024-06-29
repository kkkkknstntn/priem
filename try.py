import re

def remove_leading_zeros(s):
    return re.sub(r'^0+', '', s)

# Пример использования функции
s = '00010-23045 00 '
result = remove_leading_zeros(s)
print(result)