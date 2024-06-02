
def solve(n, m):
    if n == 0:
        return f"0 1\n0 {m}\n0 0\n0 {m-1}"
    elif m == 0:
        return f"1 0\n{n} 0\n0 0\n{n-1} 0"
    else:
        return f"0 0\n{n} {m}\n{n} 0\n0 {m}"

# Input
n, m = map(int, input().split())

# Output
print(solve(n, m))
