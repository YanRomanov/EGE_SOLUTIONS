m1 = 0
m7 = 0

count = 0

buf = int(input())

while buf != 0:
    if buf % 7 == 0 and buf % 49 != 0 and buf > m7:
        m7 = buf
    elif buf > m1:
        m1 = buf
    buf = int(input())
    count+=1

r1 = m7*m1
r = int(input())

print("Введено чиел: ", count, "\nКонтрольное значение: ", r,"\nВычисленное значение: ", r1)

if (r1 == r):
    print("Значения совпали")
else:
    print("Значения не совпали")