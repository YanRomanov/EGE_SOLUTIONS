a = []

n = 30

for i in range(0, n):
    a.append(int(input()))

x = 0
y = 0

for i in a:
    if i % 2 != 0:
        x+=i
        y+=1


print(x/y)