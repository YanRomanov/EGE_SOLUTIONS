a = []

n = 30

for i in range(0, n):
    a.append(int(input()))

sum = 0
min = a[0]
max = a[0]

for i in a:
    sum += i
    if (max < i):
        max = i
    if (min > i):
        min = i

print((max + min) / 2 - sum / n)
