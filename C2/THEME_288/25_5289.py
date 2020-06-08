a = []

n = 30

for i in range(0, n):
    a.append(int(input()))

s = 0

for i in a:
    if len(str(i)) == 2 and i / 10 > i % 2:
        s+=i


print(s)