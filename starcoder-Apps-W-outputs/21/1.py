
n,m=map(int,input().split())
a=list(map(int,input().split()))
s=0
for x in range(2,m+1):
    for y in range(2,m+1):
        if(y>=x and y>=2*x):
            flag=1
            for i in range(n):
                if not (x+i==y and (y+i)%x==0 and (y+i)//x<=m):
                    flag=0
                    break
            s+=flag
print(s)
