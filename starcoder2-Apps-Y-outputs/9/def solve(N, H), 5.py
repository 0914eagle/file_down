
def solve(N, H):
    # Write your code here
    return 'Yes' if N == 1 else 'No'

N = int(input())
H = list(map(int, input().split()))
print(solve(N, H))

