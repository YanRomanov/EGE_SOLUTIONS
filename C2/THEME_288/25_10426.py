a = []

n = 2016

for i in range(0, n):
    a.append(int(input()))

m = a[0]
s = 0
p = 0


for i in a:
    if m > i:
        m = i
    if i % 2 == 0:
        s+=i
    else:
        p+=i

if (m % 2 != 0):
    print(s)
else:
    print(p)
