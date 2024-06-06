
#python3

r,m=map(int,input().split())
a=[r]
i=1
while True:
    if a[i-1]+i==m or a[i-1]-m in a:
        print(i+1)
        break
    a.append(a[i-1]+i)
    i+=1
