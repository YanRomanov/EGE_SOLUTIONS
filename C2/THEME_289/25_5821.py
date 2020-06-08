a = []

n = 20

for i in range(0, n):
    a.append(int(input()))


max = -1

for i in a:
    if len(str(i)) == 3 and i % 2 == 0 and max < i:
        max = i

if max == -1:
    print("Не найдено")
else:
    print(max)
