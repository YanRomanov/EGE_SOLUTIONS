a = []

n = 2018

for i in range(0, n):
    a.append(int(input()))

# print(sum(1 for i in a if len(hex(i)[2:]) == len(str(i))))

k = 0

for i in range(0, n):
    if ((1 <= i and i <= 9) or
            (16 <= i and i <= 99) or
            (256 <= i and i <= 999) or
            (4096 <= i and i <= 9999)):
        k += 1

print(k)
