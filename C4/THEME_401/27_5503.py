m1 = 0
m2 = 0
m7 = 0
m14 = 0
m = 0

n = int(input())

for i in range(0, n):
    buf = int(input())
    if buf % 7 == 0 and buf % 2 != 0 and buf > m7:
        m7 = buf
    if buf % 7 != 0 and buf % 2 == 0 and buf > m2:
        m2 = buf
    if buf % 14 == 0 and buf > m14:
        m14 = buf
    elif buf > m:
        m = buf

r1 = max(m7*m2, m14*m)

print("Вычисленное контрольное значение:")
print(r1)
r = int(input())

if (r1 == r):
    print("Контроль пройден")
else:
    print("Контроль не пройден")