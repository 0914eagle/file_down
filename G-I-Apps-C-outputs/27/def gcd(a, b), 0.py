
def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def solve(N, A):
    mod = 10**9 + 7
    total = 1
    ans = 0
    for a in A:
        total = total * a % mod
    for a in A:
        ans = (ans + total * pow(a, mod - 2, mod)) % mod
    return ans

N = int(input())
A = list(map(int, input().split()))
print(solve(N, A))
