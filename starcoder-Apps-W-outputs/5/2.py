
def f(a,b):
    if b in a:
        return False
    if a[-1] == b:
        return True
    return f(a+[b],dic[b])
n,m = map(int,input().split())
dic = dict()
for i in range(1,n+1):
    dic[i] = i
for _ in range(m):
    a,b = map(int,input().split())
    dic[b] = a
for i in range(1,n+1):
    if not f([i],i):
        print(i)
