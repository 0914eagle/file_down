
def max_flowers(N, R, C, flowers):
    dp = [[0] * N for _ in range(N)]
    dp[R-1][C-1] = 1

    directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

    def is_valid(r, c):
        return 0 <= r < N and 0 <= c < N

    def can_jump(prev_petals, cur_petals):
        return cur_petals > prev_petals

    def dfs(r, c):
        if dp[r][c] != 0:
            return dp[r][c]

        max_flowers = 1
        for dr, dc in directions:
            for i in range(2, N):
                new_r, new_c = r + dr * i, c + dc * i
                if is_valid(new_r, new_c) and can_jump(flowers[r][c], flowers[new_r][new_c]):
                    max_flowers = max(max_flowers, 1 + dfs(new_r, new_c))

        dp[r][c] = max_flowers
        return max_flowers

    result = 0
    for i in range(N):
        for j in range(N):
            result = max(result, dfs(i, j))

    return result

# Read input
N = int(input())
R, C = map(int, input().split())
flowers = [list(map(int, input().split())) for _ in range(N)]

# Calculate and output the largest number of flowers the grasshopper can visit
print(max_flowers(N, R, C, flowers))
