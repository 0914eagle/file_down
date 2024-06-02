
def solve(H, A):
    return (H + A - 1) // A

H, A = map(int, input().split())
print(solve(H, A))

