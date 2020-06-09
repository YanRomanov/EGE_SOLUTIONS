a = []

n = 30


for i in range(0, n):
    a.append(int(input()))

res = 1

for i in a:
    if i < 0:
        res*=i

print(res)
