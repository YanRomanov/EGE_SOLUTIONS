
n = int(input())

n2 = 0
n5 = 0
n10 = 0

counter = 0

for i in range(0, n):
    buf = int(input())
    if buf % 5 == 0 and buf % 2 != 0:
        n5+=1
    if buf % 5 != 0 and buf % 2 == 0:
        n2+=1
    if buf % 10 == 0:
        n10+=1

    counter += 1


r1 = n5*n2 - n10*(n-n10) - n10*(n10 - 1)//2

print(r1)
