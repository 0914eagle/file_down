
n,k = map(int,input().split())
if n < k:
    print(-1)
elif k == 1:
    print("a"*n)
elif k == 26:
    s = ""
    for i in range(n):
        s += chr(ord('a') + i%2)
    print(s)
else:
    s = ""
    for i in range(k-1):
        s += chr(ord('a') + i)
    for i in range(n - k + 1):
        s += chr(ord('a') + (k-1))
    print(s)
