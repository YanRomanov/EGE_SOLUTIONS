a = []

n = 2014

for i in range(0, n):
    a.append(int(input()))

s = 0

for i in a:
    if len(str(i)) == 3 and i % 100 != 99 and i % 10 == 9:
        s+=i

if s == 0:
    print(-1)
else:
    print(s)