
for i in range(int(input())):
    n,m,h=map(int,input().split())
    x=list(map(int,input().split()))
    y=[]
    for i in range(m):
        y.append(list(map(int,input().split())))
    a=[]
    b=[]
    for i in range(len(y)):
        if x[y[i][0]-1]==x[y[i][1]-1]:
            a.append(x[y[i][0]-1])
    print(len(list(set(a))))
    print(*list(set(a)))
