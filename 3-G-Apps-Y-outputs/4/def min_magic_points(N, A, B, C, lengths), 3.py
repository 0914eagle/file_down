
def min_magic_points(N, A, B, C, lengths):
    def dfs(idx, a, b, c):
        if idx == N:
            if a == A and b == B and c == C:
                return 0
            else:
                return float('inf')
        
        key = (idx, a, b, c)
        if key in memo:
            return memo[key]
        
        # Use Extension Magic
        cost1 = dfs(idx + 1, a + 1, b, c) + 1
        
        # Use Shortening Magic
        cost2 = dfs(idx + 1, a - 1, b, c) + 1 if a >= 2 else float('inf')
        
        # Use Composition Magic
        cost3 = dfs(idx + 1, a + lengths[idx], b, c) + 10
        cost4 = dfs(idx + 1, a, b + lengths[idx], c) + 10
        cost5 = dfs(idx + 1, a, b, c + lengths[idx]) + 10
        
        memo[key] = min(cost1, cost2, cost3, cost4, cost5)
        
        return memo[key]
    
    memo = {}
    result = dfs(0, 0, 0, 0)
    
    return result

# Sample Input
N = 5
A, B, C = 100, 90, 80
lengths = [98, 40, 30, 21, 80]

print(min_magic_points(N, A, B, C, lengths))
