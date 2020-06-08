a = []

n = 23

for i in range(0, n):
    a.append(int(input()))


max = 1500

for i in a:
    if max < i <= 1800:
        max = i

print(max)
