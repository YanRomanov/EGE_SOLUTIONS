a = []

n = 40

for i in range(0, n):
    a.append(int(input()))

max = -1

for i in a:
    if len(str(max)) == 2 and i % 3 != 0 and max < a:
        max = a

if max == -1:
    print("Не найдено")
else:
    print(max)
