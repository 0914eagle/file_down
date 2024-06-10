
n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

a.sort()
b.sort()

def calc(a, b):
    res = 0
    for i in range(len(a)):
        res += a[i] * b[i]
    return res

print(calc(a, b) % 998244353)

