
n = int(input())

max1 = 0
max2 = 0
max13 = 0
max26 = 0

counter = 0

for i in range(0, n):
    buf = int(input())
    if buf % 13 == 0 and buf % 2 != 0 and max13 < buf:
        max13 = buf
    if buf % 13 != 0 and buf % 2 == 0 and max2 < buf:
        max2 = buf
    if buf % 26 == 0 and buf > max26:
        max26 = buf
    elif buf > max1:
        max1 = buf
    counter += 1

r = int(input())

r1 = max(max26*max1, max13*max2)

print("Вычисленное значение: ", r1)

if (r1 == r):
    print("Контроль пройден")
else:
    print("Контроль не пройден")