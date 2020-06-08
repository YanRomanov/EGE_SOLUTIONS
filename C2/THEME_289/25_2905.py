a = []

n = 30

for i in range(0, n):
    a.append(int(input()))


max_neg = 0

for i in a:
    if i < 0 and max_neg > i:
        max_neg = i

print(max_neg)
