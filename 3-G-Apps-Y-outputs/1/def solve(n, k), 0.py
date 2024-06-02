
def solve(n, k):
    if n % 2 != k % 2 or k > n:
        print("NO")
    elif n < k:
        print("NO")
    else:
        print("YES")
        if n % 2 == 0:
            print(" ".join(["2"] * (k - 1)) + " " + str(n - 2 * (k - 1)))
        else:
            print(" ".join(["1"] * (k - 1)) + " " + str(n - (k - 1)))

t = int(input())
for _ in range(t):
    n, k = map(int, input().split())
    solve(n, k)
