
n,m,k = map(int,input().split())

matrix = []
for i in range(n):
    matrix.append([])
    for j in range(m):
        matrix[i].append(0)

count = 1
path = []

if n == 1:
    for i in range(m-k):
        path.append(count)
        count+=1
    for i in range(k):
        print(path[i],end = ' ')

elif m == 1:
    for i in range(n-k):
        path.append(count)
        count+=1
    for i in range(k):
        print(path[i],end = ' ')
else:
    while k!=0:
        if n==2 and k%2==1:
            matrix[0][0] = count
            path.append(count)
            count+=1
            k-=1
            break
        elif m ==2 and k%2==1:
            matrix[0][0] = count
            path.append(count)
            count+=1
            k-=1
            break
        for i in range(n):
            for j in range(m):
                if matrix[i][j]!=0:
                    continue
                else:
                    matrix[i][j] = count
                    path.append(count)
                    count+=1
                    k-=1
                    break
            if k == 0:
                break
        for i in range(m):
            for j in range(n):
                if matrix[j][i]!=0:
                    continue
                else:
                    matrix[j][i] = count
                    path.append(count)
                    count+=1
                    k-=1
                    break
            if k == 0:
                break
    print(sum(path))
    for i in path:
        print(f'({1},{path.index(i)+1}) ',end = '')
