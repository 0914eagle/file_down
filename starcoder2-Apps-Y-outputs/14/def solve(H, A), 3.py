
def solve(H, A):
    return H // A + (H % A > 0)

H, A = map(int, input().split())
print(solve(H, A))

