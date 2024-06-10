
def solve(n, a):
    if n == 1:
        return 0
    if n == 2:
        if a[0] == 2 and a[1] == 2:
            return 1
        else:
            return 0
    if a[0] == 2 and a[1] == 2:
        return 1 + solve(n - 2, a[2:])
    else:
        return solve(n - 1, a[1:])

n = int(input())
a = list(map(int, input().split()))
print(solve(n, a))

