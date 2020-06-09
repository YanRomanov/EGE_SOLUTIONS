x = int(input())
y = int(input())

for i in range(1, 8):
    for j in range(1, 8):
        dx = abs(i - x)
        dy = abs(j - y)
        if dx == 1 and dy == 2 or dx == 2 and dy == 1:
            print(i, " ", j)
