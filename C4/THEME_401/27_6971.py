
n = int(input())

max1 = 0
max2 = 0
max3 = 0
max4 = 0
max5 = 0
max6 = 0
counter = 0

for i in range(0, n):
    buf = int(input())
    if buf % 2 == 0 and buf % 5 != 0:
        if max1 < buf:
            max2 = max1
            max1 = buf
        elif max2 < buf:
            max2 = buf
    if buf % 2 != 0 and buf % 5 == 0:
        if max3 < buf:
            max4 = max3
            max3 = buf
        elif max4 < buf:
            max4 = buf
    if buf % 2 != 0 and buf % 5 != 0:
        if max5 < buf:
            max6 = max5
            max5 = buf
        elif max6 < buf:
            max6 = buf
    counter += 1

d = [0,0 , 0, 0,0,0 ,0]

d[0] = max1*max2
d[1] = max3*max4
d[2] = max5*max6
d[3] = max5*max1
d[4] = max5*max3

r = int(input())

r1 = max(d)

print("Получено чиел: ", counter, "\nПринято контрольное значение: ", r,"\nВычисленное значение: ", r1)

if (r1 == r):
    print("Контроль пройден")
else:
    print("Контроль не пройден")