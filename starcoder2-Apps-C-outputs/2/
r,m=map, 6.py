
r,m=map(int,input().split())
a=[r]
for i in range(1,10000):
    a.append(a[i-1]+i+1)
    if a[i]==m or a[i]-a[i-1]==m:
        print(i+1)
        break
