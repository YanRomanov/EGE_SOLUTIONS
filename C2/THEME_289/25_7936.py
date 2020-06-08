a = []

n = 6

for i in range(0, n):
    a.append(int(input()))

k = 0

for i in a:
    if i % 2 != 0:
        k+=1

m = 0
if k <= n - k:
    for i in a:
        if m < i and i % 2 == 0:
            m = i
else:
    for i in a:
        if m < i and i % 2 != 0:
            m = i

print(m)
