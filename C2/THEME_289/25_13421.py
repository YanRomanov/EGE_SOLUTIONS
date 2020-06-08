a = []

n = 2017

for i in range(0, n):
    a.append(int(input()))


m = 0

for i in a:
    if 512 >= i > m and i % 8 == 4:
        m = i

print(m)
