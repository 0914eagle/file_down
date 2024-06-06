


n,k = map(int,input().split())
lis = []
for i in range(n):
    x = list(map(int,input().split()))
    lis.append(x)
#print(lis)
lis1 = []
for i in range(n):
    x = lis[i][0] + lis[i][1] + lis[i][2]
    if x <= 2:
        lis1.append(x)
if len(lis1) > 0:
    print('YES')
else:
    print('NO')
