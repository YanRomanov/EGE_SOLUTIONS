a = []

n = 30



for i in range(0, n):
    a.append(int(input()))

res = 0

for i in a:
    if i < 0:
        res += i

if res == 0:
    print("Not Found")
else:
    print(res)
