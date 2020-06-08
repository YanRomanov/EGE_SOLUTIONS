a = []

n = 2017

for i in range(0, n):
    a.append(int(input()))


m = 0

for i in a:
    if 4096 >= i > m and i % 16 == 3:
        m = i

print(m)
