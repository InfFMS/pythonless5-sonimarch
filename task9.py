import random

# Напишите программу, которая удаляет дубликаты из списка длины N.
# Пример работы:
# Пример: ввод N = 8
# [10, 20, 10, 20, 30, 40, 30, 50]
# После удаления дублей:  [10, 20, 30, 40, 50]

s = [random.randint(0, 10) for i in range(int(input()))]
i = 0
while i < len(s):
    if s.count(s[i]) >= 2:
        del s[i]
    else:
        i += 1
print(s)