
def solve():
    N, K = map(int, input().split())
    heights = sorted([int(input()) for _ in range(N)])
    min_diff = float('inf')
    for i in range(N-K+1):
        diff = heights[i+K-1] - heights[i]
        if diff < min_diff:
            min_diff = diff
    print(min_diff)
solve()

