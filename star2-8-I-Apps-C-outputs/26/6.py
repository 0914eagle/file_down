
n,m = map(int,input().split())
a = list(map(int,input().split()))
w = list(map(int,input().split()))
def solve(n,m,a,w):
    for i in range(n):
        w[i] = w[i] + m * a[i]
    return w

for i in solve(n,m,a,w):
    print(i % 998244353)

