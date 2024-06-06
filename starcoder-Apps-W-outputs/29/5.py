
#A
n,k=map(int,input().split())
a=list(map(int,input().split()))
if k<max(a):
    print("NO")
else:
    print("YES")
    for i in range(n):
        print(' '.join(map(str, [k-a[i]+1 for _ in range(a[i])])))
