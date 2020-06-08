a = []

n = 2000

for i in range(0, n):
    a.append(int(input()))

k = 0

for i in range(1, n - 1):
    if a[i] % 4 == 0 and a[i + 1] % 4 == 0:
        k+=1

print(k)
