a = []

n = 70

for i in range(0, n):
    a.append(int(input()))

min = -1

for i in a:
    if i > 0 and min % 2 != 0 and (min == -1 or min > i):
        min = i

print(min)
