a = []

n = 23

for i in range(0, n):
    a.append(int(input()))


max = 1600

for i in a:
    if 1600 <= i <= 1800 and max < i:
        max = i

print(max)
