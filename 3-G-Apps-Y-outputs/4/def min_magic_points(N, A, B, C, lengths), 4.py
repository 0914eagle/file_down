
def min_magic_points(N, A, B, C, lengths):
    def dfs(a, b, c, idx):
        nonlocal min_points
        if idx == N:
            if a != A or b != B or c != C:
                return
            min_points = min(min_points, points)
            return

        # Use Extension Magic
        dfs(a + 1, b, c, idx + 1)
        dfs(a, b + 1, c, idx + 1)
        dfs(a, b, c + 1, idx + 1)

        # Use Shortening Magic
        if a >= 2:
            dfs(a - 1, b, c, idx + 1)
        if b >= 2:
            dfs(a, b - 1, c, idx + 1)
        if c >= 2:
            dfs(a, b, c - 1, idx + 1)

        # Use Composition Magic
        for i in range(idx + 1, N):
            for j in range(i + 1, N):
                new_lengths = lengths[:idx] + [lengths[i] + lengths[j]] + lengths[idx + 1:i] + lengths[i + 1:j] + lengths[j + 1:]
                dfs(a, b, c, idx + 1)

    min_points = float('inf')
    points = 0
    dfs(0, 0, 0, 0)
    return min_points

# Input
N, A, B, C = map(int, input().split())
lengths = [int(input()) for _ in range(N)]

# Output
print(min_magic_points(N, A, B, C, lengths))
