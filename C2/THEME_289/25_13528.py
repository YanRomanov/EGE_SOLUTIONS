a = []

n = 2016

for i in range(0, n):
    a.append(int(input()))


m = 0

for i in a:
    if 256 > i >= 16 and i > m:
        m = i

print(m)
