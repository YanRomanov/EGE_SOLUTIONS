
n = int(input())

n2 = 0
n31 = 0
n62 = 0

counter = 0

for i in range(0, n):
    buf = int(input())
    if buf % 31 == 0 and buf % 2 != 0:
        n31+=1
    if buf % 31 != 0 and buf % 2 == 0:
        n2+=1
    if buf % 62 == 0:
        n62+=1

    counter += 1


r1 = n*(n - 1)//2 - n31*n2 - n62*(n-n62) - n62*(n62 - 1)//2

print(r1)
