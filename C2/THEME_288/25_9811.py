a = []

n = 2015

for i in range(0, n):
    a.append(int(input()))

k = -1

for i in range(1, n - 1):
    if (a[i] < a[i - 1]) and (a[i] < a[i + 1]):
        if k == -1 or a[i] < k:
            k = a[i]

print(k)
