
def sds(r,m):
    a = [r]
    for i in range(1,10000):
        a.append(a[i-1]+i)
        if a[i] == m:
            return i+1
        elif a[i] > m:
            return i+1
    for i in range(1,10000):
        a.append(a[i-1]+i)
        if a[i] == m:
            return i+1
        elif a[i] > m:
            return i+1

r,m = map(int,input().split())
print(sds(r,m))
