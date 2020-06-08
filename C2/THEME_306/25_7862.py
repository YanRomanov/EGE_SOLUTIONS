a = []

n = 20

for i in range(0, n):
    a.append(int(input()))

k = 0

for i in range(0, n-1):
    if((a[i] + a[i + 1] % 2) == 0) and ((a[i] + a[i + 1]) % 4 != 0):
        k+=1

print(k)