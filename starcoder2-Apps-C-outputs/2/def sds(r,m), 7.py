
def sds(r,m):
    a=[r]
    i=1
    while True:
        if a[-1]+i in a or a[-1]-i in a:
            i+=1
        else:
            a.append(a[-1]+i)
            if a[-1]==m or a[-1]-i==m:
                return len(a)
            i=1

r,m=map(int,input().split())
print(sds(r,m))
