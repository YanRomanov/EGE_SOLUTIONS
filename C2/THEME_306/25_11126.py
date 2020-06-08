a = []

n = 50

for i in range(0, n):
    a.append(int(input()))

k = 0

for i in range(1, n - 1):
    if len(str(a[i])) == 2 and len(str(a[i + 1])) == 2:
        k+=1

print(k)
