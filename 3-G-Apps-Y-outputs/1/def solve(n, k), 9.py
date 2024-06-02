
def solve(n, k):
    if n % 2 != k % 2 or k > n:
        return "NO"
    else:
        return "YES\n" + " ".join([str(n // k)] * (k - 1) + [str(n // k + n % k)])

t = int(input())
for _ in range(t):
    n, k = map(int, input().split())
    print(solve(n, k))
