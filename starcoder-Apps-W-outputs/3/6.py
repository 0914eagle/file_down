
for _ in range(int(input())):
    n,k,q = map(int,input().split())
    a = []
    for i in range(n):
        l,r = map(int,input().split())
        a.append((l,1))
        a.append((r+1,-1))
    a.sort()
    s = 0
    ans = 0
    for i in range(len(a)-1):
        if a[i][1] == 1:
            s+=1
        if s>=k:
            ans+=a[i+1][0]-a[i][0]
        else:
            s-=a[i][1]
    l,r = map(int,input().split())
    print(ans-(r-l+1))
