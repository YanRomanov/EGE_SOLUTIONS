a = []

n = 6

for i in range(0, n):
    a.append(int(input()))

k = 0

for i in a:
    if i % 2 == 1:
        k+=1

if k % 2 == 0:
    print(k)
else:
    print(n)
