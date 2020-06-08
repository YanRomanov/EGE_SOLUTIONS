a = []

n = 30

for i in range(0, n):
    a.append(int(input()))

# print(sum(1 for i in a if len(oct(i)[2:]) == len(str(i))))

s = 0

for i in a:
    if i < 200 and i % 5 == 0:
        s+=i

for i in range(0, n):
    if a[i] < 200 and a[i] % 5 == 0:
        a[i] = s
    print(a[i])

