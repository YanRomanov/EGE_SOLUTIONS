a = []

n = 2016

for i in range(0, n):
    a.append(int(input()))

k = 0

for i in range(0, n - 2):
    if a[i] == (a[i+1] + a[i+2])/2:
        k+=1

print(k)