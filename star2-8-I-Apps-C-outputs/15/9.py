
n = int(input())
a = list(map(int, input().split()))

m = min(a)
if m == 0:
    print(-1)
    exit()

def gcd(x, y):
    if x == 0:
        return y
    return gcd(y % x, x)

res = 0
for i in a:
    res += i // m

print(res)

