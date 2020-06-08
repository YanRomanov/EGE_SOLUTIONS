a = []

n = 30

for i in range(0, n):
    a.append(int(input()))


maxe = 0
maxo = 0

for i in a:
    if i % 2 == 0:
        if maxe < i:
            maxe = i
    else:
        if maxo < i:
            maxo = i

print(maxe - maxo)
