a = []

n = 2017

for i in range(0, n):
    a.append(int(input()))


k = 0

for i in a:
    if 16 <= i < 256 and 10 <= i % 16 <= 15:
        k+=1

print(k)
