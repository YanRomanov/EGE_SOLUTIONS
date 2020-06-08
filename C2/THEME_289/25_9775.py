a = []

n = 6

for i in range(0, n):
    a.append(int(input()))

k = 0

for i in range(1, n - 1):
    if a[i - 1] < a[i] > a[i + 1] and k < a[i]:
        k = a[i]

print(k)
