a = []

n = 30

for i in range(0, n):
    a.append(int(input()))

min = 100

for i in a:
    if 20 < i < min:
        min = i

print(min)
