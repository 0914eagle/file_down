

n,m = map(int,input().split())

arr = [0]*n

for i in range(m):
    x,y = map(int,input().split())
    arr[x-1] += 1
    arr[y-1] += 1
    print(n*n - (n-arr[x-1])*(n-arr[y-1]))
