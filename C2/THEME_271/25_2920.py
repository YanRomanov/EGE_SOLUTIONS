a = []

n = 30



for i in range(0, n):
    a.append(int(input()))


index = -1

for i in range(1, n-1):
    if a[i-1] < a[i] > a[i+1]:
        index = i
        break

if index == -1:
    print("Not Found")
else:
    print(index-1, " ", index, " ", index+1)
