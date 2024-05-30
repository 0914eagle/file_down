
def solve(n, k):
    if n % 2 != k % 2 or k > n:
        print("NO")
    else:
        print("YES")
        if n % 2 == 0:
            print(" ".join([str(n // k)] * k))
        else:
            print(" ".join([str(1)] + [str((n-1) // (k-1))] * (k-1)))

t = int(input())
for _ in range(t):
    n, k = map(int, input().split())
    solve(n, k)
