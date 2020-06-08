a = []

n = 2016

for i in range(0, n):
    a.append(int(input()))


m = a[0]

for i in a:
    if(i % 2 == m % 2 and i > m) or (i % 2 == 0 and m % 2 == 1):
        m = i


print(m)
