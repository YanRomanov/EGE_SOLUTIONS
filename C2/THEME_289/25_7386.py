a = []

n = 20

for i in range(0, n):
    a.append(int(input()))


max = 150

for i in a:
    if 175 > i > max:
        max = i


print(max)
