
def solve(H, A):
    return (H - 1) // A + 1

H, A = map(int, input().split())
print(solve(H, A))

