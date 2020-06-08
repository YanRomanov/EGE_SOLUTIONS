a = []

n = 30

for i in range(0, n):
    a.append(int(input()))


oldest = a[0]
oldest_index = 0

for i in range(1, n):
    if oldest > a[i]:
        oldest = a[i]
        oldest_index = i

print(oldest_index)
