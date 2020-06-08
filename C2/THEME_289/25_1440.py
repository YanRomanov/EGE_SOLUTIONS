a = []

n = 2018

for i in range(0, n):
    a.append(int(input()))


m = 0

for i in a:
    if i % 10 == i % 16 and m < i:
        m = i

print(m)
