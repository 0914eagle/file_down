
n, k = map(int, input().split())
if n == k:
    print("1"*n)
elif k == 1:
    print("0"*(n-1) + "1")
else:
    print("0"*(k-1) + "1"*(n-k+1))

