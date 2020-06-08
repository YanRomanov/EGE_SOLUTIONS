a = []

n = 20

for i in range(0, n):
    a.append(int(input()))

k = 0

for i in range(0, n-1):
    if((a[i] % 3) == 0) and ((a[i + 1] % 3) == 0):
        k+=1

print(k)