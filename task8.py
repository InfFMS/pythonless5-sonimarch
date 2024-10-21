import random

# Заполнить массив длины N случайными числами в диапазоне от 10 до 100000 и
# отобрать в другой массив все числа, которые состоят из одинаковых цифр.
# Используйте для этого логическую функцию.
# Пример: ввод N = 4
# [12, 77, 5555, 97]
# Вывод: [77, 5555]

def num(n):
    n = str(n)
    if len(set(n)) == 1:
        return True
    else:
        return False


d = []
s = [random.randint(10, 100000) for i in range(int(input()))]
for i in s:
    if num(i):
        d.append(i)
print(d)