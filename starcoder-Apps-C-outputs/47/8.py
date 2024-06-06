
n,k=map(int,input().split())
for i in range(1,n+1):
    if (n+1-i)<=(k-1):
        print("a"*i+"b"*(n-i))
        break
else:
    print(-1)
