a = []

n = 5

for i in range(0, n):
    a.append(int(input()))


max1 = a[0]
max2 = a[1]

if max2 > max1:
    max1, max2 = max2, max1

for i in a:
    if max1 < i:
        max2 = max1
        max1 = i
    elif max2 < i:
        max2 = i

print(max2)
