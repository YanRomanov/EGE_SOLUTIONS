a = []

n = 2017

for i in range(0, n):
    a.append(int(input()))

s = 0

for i in a:
    if i > 255 and i < 4096 and i > 9:
        s+=i


print(s)

