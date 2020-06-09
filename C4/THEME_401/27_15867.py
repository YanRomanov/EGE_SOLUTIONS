
n = int(input())

n2 = 0
n7 = 0
n14 = 0

counter = 0

for i in range(0, n):
    buf = int(input())
    if buf % 7 == 0 and buf % 2 != 0:
        n7+=1
    if buf % 7 != 0 and buf % 2 == 0:
        n2+=1
    if buf % 14 == 0:
        n14+=1

    counter += 1


r1 = n*(n - 1)//2 - n7*n2 - n14*(n14 - 1)//2 - n14*(n-n14)

print(r1)
