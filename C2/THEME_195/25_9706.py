a = []

n = 30

for i in range(0, n):
    a.append(int(input()))

min = 10001

for i in a:
    if len(str(i)) == 3 and i % 7 != 0 and min > i:
        min = i

if min < 10001:
    print(min)
else:
    print("Не найдено")