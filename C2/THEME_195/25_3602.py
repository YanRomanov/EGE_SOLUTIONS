a = []

n = 50

for i in range(0, n):
    a.append(int(input()))

j = -1

for i in a:
    if i < 0:
        j = i
        break

if j >= 0:
    print(j)
else:
    print("Не найдено")