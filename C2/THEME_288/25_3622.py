a = []

n = 40

for i in range(0, n):
    a.append(int(input()))

s = a[0]
l = 1
sMax = 0
lMax = 0

for i in range(1, n):
    if (a[i - 1] < a[i]):
        s += a[i]
        l += 1
    else:
        if l > lMax:
            sMax = s
            lMax = l
        l = 1
        s = a[i]

if l > lMax:
    sMax = s

print(sMax)
