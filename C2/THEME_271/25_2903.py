a = []

n = 30



for i in range(0, n):
    a.append(int(input()))

len = 1
max_len = 0

for i in range(0, n - 1):
    if a[i] < a[i+1]:
        len+=1
    else:
        if max_len < len:
            max_len = len
        len = 1

if max_len < len:
    max_len = len

print(max_len)
