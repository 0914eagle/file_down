
n = int(input())
a = list(map(int,input().split()))
for i in range(n):
    if i<n-1:
        print(1,i+2)
    else:
        print(1,1)
