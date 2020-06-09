a = []

n = 20

for i in range(0, n):
    a.append(int(input()))

min = 1001

for i in a:
    if 0 < i < min and i % 3 != 0:
        min = i


print(min)
