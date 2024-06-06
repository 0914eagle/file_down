
n = int(input())
a = [int(input()) for i in range(2**n)]
a.sort()
b = [[0 for i in range(n)] for j in range(2**n)]
for i in range(2**n):
    temp = bin(a[i])[2:]
    for j in range(len(temp)):
        b[i][n-len(temp)+j-1] = temp[j]
b = [list(map(int,i)) for i in b]
b = b[::-1]
c = [0 for i in range(n)]
for i in range(n):
    temp = [b[j][i] for j in range(2**n)]
    if temp.count(1) == 0:
        if i < n-1:
            for j in range(2**n):
                if b[j][i+1] == 1:
                    b[j][i] = 1
        else:
            print('impossible')
            break
    else:
        c[i] = a[-1]
        a.remove(c[i])
        for j in range(2**n):
            if b[j][i] == 1:
                for k in range(i+1,n):
                    b[j][k] = 0
                c[i] -= a[j]

if 'impossible' not in c:
    for i in c:
        print(i)
