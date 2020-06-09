a = []

n = 40

for i in range(0, n):
    a.append(int(input()))

min = -1

for i in a:
    if i > 0 and (min == -1 or min > i):
        min = i

if min != -1:
    print(min)
else:
    print("Не найдено")