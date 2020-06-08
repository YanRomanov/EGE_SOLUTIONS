a = []

n = 30

for i in range(0, n):
    a.append(int(input()))

k = 0

for i in range(1, n - 1):
    if a[i] % 13 == 0 or a[i + 1] % 3 == 0:
        k+=1

print(k)
