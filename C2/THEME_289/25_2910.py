a = []

n = 10

for i in range(0, n):
    a.append([])
    for j in range(0, n):
        a[i].append(int(input()))

print(a)
sum = 0

for i in range(0, n):
    max = a[i][0]
    for j in range(0, n):
        if max < a[i][j]:
            max = a[i][j]
    sum += max

print(sum)
