a = []

n = 30

for i in range(0, n):
    a.append(int(input()))

me = 0
mn = 0

for i in a:
    if i % 2 == 0:
        if me < i:
            me = i
    else:
        if mn < i:
            mn = i


print(me - mn)
