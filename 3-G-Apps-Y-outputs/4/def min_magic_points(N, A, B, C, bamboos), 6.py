
def min_magic_points(N, A, B, C, bamboos):
    def dfs(idx, a, b, c):
        if idx == N:
            return abs(a - A) + abs(b - B) + abs(c - C) if min(a, b, c) > 0 else float('inf')
        
        res = float('inf')
        res = min(res, dfs(idx + 1, a, b, c))  # Skip current bamboo
        
        res = min(res, 1 + dfs(idx + 1, a + bamboos[idx], b, c))  # Use Extension Magic
        res = min(res, 1 + dfs(idx + 1, a, b + bamboos[idx], c))  # Use Extension Magic
        res = min(res, 1 + dfs(idx + 1, a, b, c + bamboos[idx]))  # Use Extension Magic
        
        if a + b + c >= 2:
            res = min(res, 10 + dfs(idx + 1, a + b, c, 0))  # Use Composition Magic
            res = min(res, 10 + dfs(idx + 1, a, b + c, 0))  # Use Composition Magic
            res = min(res, 10 + dfs(idx + 1, a, b, c + a))  # Use Composition Magic
        
        if bamboos[idx] >= 2:
            res = min(res, 1 + dfs(idx + 1, a + bamboos[idx] - 2, b, c))  # Use Shortening Magic
            res = min(res, 1 + dfs(idx + 1, a, b + bamboos[idx] - 2, c))  # Use Shortening Magic
            res = min(res, 1 + dfs(idx + 1, a, b, c + bamboos[idx] - 2))  # Use Shortening Magic
        
        return res
    
    return dfs(0, 0, 0, 0)

# Input
N, A, B, C = map(int, input().split())
bamboos = [int(input()) for _ in range(N)]

# Output
print(min_magic_points(N, A, B, C, bamboos))
