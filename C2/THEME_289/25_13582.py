a = []

n = 2016

for i in range(0, n):
    a.append(int(input()))


m = 0

for i in a:
    if i > m and i % 16 == 14:
        m = i

print(m)
