
def sds(r,m):
    if r==m:
        return 1
    a=[r]
    i=1
    while True:
        i+=1
        if i-1 in a:
            a.append(i)
        else:
            for j in range(len(a)):
                if i-a[j] in a:
                    a.append(i)
                    break
        if i==m or i-m in a:
            return i
r,m=map(int,input().split())
print(sds(r,m))
