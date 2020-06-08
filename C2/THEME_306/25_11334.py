a = []

n = 30

for i in range(0, n):
    a.append(int(input()))

k = 0

for i in range(1, n - 1):
    if a[i] % 10 == 6 and a[i + 1] % 10 == 6:
        k+=1

print(k)
