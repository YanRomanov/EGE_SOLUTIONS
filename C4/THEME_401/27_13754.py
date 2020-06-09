
n = int(input())

m2 = 0
m13 = 0
m26 = 0

counter = 0

for i in range(0, n):
    buf = int(input())
    if buf % 13 == 0 and buf % 2 != 0:
        m13+=1
    if buf % 13 != 0 and buf % 2 == 0:
        m2+=1
    if buf % 26 == 0:
        m26+=1

    counter += 1


r1 = m13*m2 + m26*(n-m26) + m26*(m26-1)//2

print(r1)
