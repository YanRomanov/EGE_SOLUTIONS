a = []

n = 2018

for i in range(0, n):
    a.append(int(input()))

# print(sum(1 for i in a if len(oct(i)[2:]) == len(str(i))))

k = 0

for i in range(0, n):
    if ((1 <= i and i <= 7) or
        (10 <= i and i <= 63) or
        (100 <= i and i <= 511) or
        (1000 <= i and i <= 4095) or
        (10000 <= i and i <= 32767)):
        k += 1

print(k)
