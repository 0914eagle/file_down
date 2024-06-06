
n, k = map(int, input().split())
data = []
for i in range(n):
    data.append(list(map(int, input().split())))

if k == 2:
    num = 0
    for i in range(n):
        if data[i][0] == 1 and data[i][1] == 1:
            num += 1
        if num > 1:
            print('NO')
            break
    else:
        print('YES')

elif k == 3:
    num = 0
    for i in range(n):
        if data[i][0] == 1 and data[i][1] == 1:
            num += 1
        if data[i][0] == 1 and data[i][2] == 1:
            num += 1
        if data[i][1] == 1 and data[i][2] == 1:
            num += 1
        if num > 1:
            print('NO')
            break
    else:
        print('YES')

elif k == 4:
    num = 0
    for i in range(n):
        if data[i][0] == 1 and data[i][1] == 1:
            num += 1
        if data[i][0] == 1 and data[i][2] == 1:
            num += 1
        if data[i][0] == 1 and data[i][3] == 1:
            num += 1
        if data[i][1] == 1 and data[i][2] == 1:
            num += 1
        if data[i][1] == 1 and data[i][3] == 1:
            num += 1
        if data[i][2] == 1 and data[i][3] == 1:
            num += 1
        if num > 1:
            print('NO')
            break
    else:
        print('YES')

else:
    print('NO')
