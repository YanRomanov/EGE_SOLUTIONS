a = []

n = 30

for i in range(0, n):
    a.append(int(input()))

s = 0

for i in a:
    if i < 0:
        s += i

if s == 0:
    print("Negative numburs not found")
else:
    print(s)