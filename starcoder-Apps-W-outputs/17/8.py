
n = int(input())
arr = list(map(int,input().split()))
max_ = max(arr)
if max_>n-1:
    print("NO")
else:
    print("YES",max_)
    print(n-1)
    for i in range(1,n):
        print(i,i+1)
