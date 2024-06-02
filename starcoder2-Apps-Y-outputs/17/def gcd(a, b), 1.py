
n = int(input())
a = list(map(int, input().split()))

def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)

def lcm(a, b):
    return a * b // gcd(a, b)

l = a[0]
for i in range(1, n):
    l = lcm(l, a[i])

print(l, l // a[0])

