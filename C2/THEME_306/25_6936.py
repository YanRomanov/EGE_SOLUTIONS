a = []

n = 2014

for i in range(0, n):
    a.append(int(input()))

d = abs(a[1] - a[0])

k = 0

for i in range(0, n - 1):
    if (d < abs(a[i + 1] - a[i])):
        d = abs(a[i + 1] - a[i])
        k = i

print(a[k], " ", a[k + 1])
