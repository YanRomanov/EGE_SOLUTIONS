
n = int(input())

n2 = 0
n17 = 0
n34 = 0

count = 0

for i in range(0, n):
    buf = int(input())
    if buf % 17 == 0 and buf % 2 != 0:
        n17+=1
    if buf % 17 != 0 and buf % 2 == 0:
        n2+=1
    if buf % 34 == 0:
        n34 += 1
    count+=1

res = (n*(n-1)//2) - n2*n17 - n34*(n-n34) - (n34*(n34-1))//2

print(res)