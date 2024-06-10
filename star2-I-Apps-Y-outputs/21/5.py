
n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

a.sort()
b.sort()

MOD = 998244353

def calc(a, b):
    res = 0
    for x in a:
        for y in b:
            res += x * y
            res %= MOD
    return res

print(calc(a, b))

