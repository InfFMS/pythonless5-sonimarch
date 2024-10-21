# Посчитайте угол между двумя векторами размерности N.
# Примечание: Вспомните определение скалярного произведения.
# Изначально вектор заполните рандомными числами.
# Пример: N =3
# вектор a = [0, 1, 0]
# вектор b = [1, 0, 0]
# Угол = 90
import math

n = int(input())
d = [1 for i in range(n)]
s = [list(map(int, input().split())) for i in range(n)]
for i in s:
    for j in range(n):
        d[j] *= i[j]

g = 1
l = 0
for i in s:
    for j in i:
        l += j ** 2
    g *= l
    l = 0

cos = sum(d) / g
print(math.acos(cos))