a = []

n = 10

for i in range(0, n):
    a.append([])
    for j in range(0, n):
        a[i].append(int(input()))

is_magic = True

control = sum(a[0])

# rows
for i in range(0, n):
    if sum(row[i] for row in a) != control:
        is_magic = False
        break
# cols
if is_magic:
    for i in range(0, n):
        tmp = 0
        for j in range(0, n):
            tmp += a[j][i]
        if tmp != control:
            is_magic = False
            break

# diagonals
if is_magic:
    main_diag = 0
    collateral_diag = 0

    for i in range(0, n):
        main_diag += a[i][i]
        collateral_diag += a[-i][-i]
    if main_diag != control or collateral_diag != control:
        is_magic = False

if is_magic:
    print("Magic")
else:
    print("Not magic")
