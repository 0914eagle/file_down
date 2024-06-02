
def solve(n, k):
    if n % 2 != k % 2 or k > n:
        print("NO")
    else:
        if n >= k:
            print("YES")
            print(" ".join([str(n // k)] * (k - 1) + [str(n // k + n % k)]))
        else:
            print("YES")
            print(" ".join(["1"] * (k - 1) + [str(n)]))

t = int(input())
for _ in range(t):
    n, k = map(int, input().split())
    solve(n, k)
