a = []

n = 20

for i in range(0, n):
    a.append(int(input()))

k = 0

for i in range(1, n - 1):
    if a[i] % 10 == 2 or a[i + 1] % 10 == 2:
        k+=1

print(k)
