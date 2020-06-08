a = []

n = 25

for i in range(0, n):
    a.append(int(input()))


min = 50
j = 0

for i in a:
    if min > i > 40:
        min = i
        j = i

print(min)
