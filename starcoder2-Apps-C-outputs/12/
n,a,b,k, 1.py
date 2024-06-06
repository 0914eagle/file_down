
n,a,b,k = map(int,input().split())
s = input()

if k == 1:
    print((a-b)%(10**9+9))
else:
    if s[0] == '+':
        print((a**k-b**k)%(10**9+9))
    else:
        print((b**k-a**k)%(10**9+9))
