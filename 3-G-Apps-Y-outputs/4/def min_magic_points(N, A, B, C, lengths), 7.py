
def min_magic_points(N, A, B, C, lengths):
    def dfs(a, b, c, idx):
        if idx == N:
            return abs(a - A) + abs(b - B) + abs(c - C) - 30  # Subtract 30 as the first composition magic is free
        cost1 = dfs(a, b, c, idx + 1)
        cost2 = dfs(a + lengths[idx], b, c, idx + 1) + 2
        cost3 = dfs(a, b + lengths[idx], c, idx + 1) + 2
        cost4 = dfs(a, b, c + lengths[idx], idx + 1) + 2
        cost5 = dfs(a + lengths[idx], b + lengths[idx], c, idx + 1) + 12
        cost6 = dfs(a + lengths[idx], b, c + lengths[idx], idx + 1) + 12
        cost7 = dfs(a, b + lengths[idx], c + lengths[idx], idx + 1) + 12
        cost8 = dfs(a + lengths[idx], b + lengths[idx], c + lengths[idx], idx + 1) + 22
        return min(cost1, cost2, cost3, cost4, cost5, cost6, cost7, cost8)

    return dfs(0, 0, 0, 0)

# Sample Input
N = 5
A, B, C = 100, 90, 80
lengths = [98, 40, 30, 21, 80]

print(min_magic_points(N, A, B, C, lengths))
