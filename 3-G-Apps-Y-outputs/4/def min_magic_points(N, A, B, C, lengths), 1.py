
def min_magic_points(N, A, B, C, lengths):
    def dfs(a, b, c, idx):
        if idx == N:
            return abs(a - A) + abs(b - B) + abs(c - C) - 30 if min(a, b, c) > 0 else float('inf')
        
        # Case 1: Do not use the current bamboo
        ans1 = dfs(a, b, c, idx + 1)
        
        # Case 2: Use the current bamboo for A
        ans2 = dfs(a + lengths[idx], b, c, idx + 1) + (10 if a > 0 else 0)
        
        # Case 3: Use the current bamboo for B
        ans3 = dfs(a, b + lengths[idx], c, idx + 1) + (10 if b > 0 else 0)
        
        # Case 4: Use the current bamboo for C
        ans4 = dfs(a, b, c + lengths[idx], idx + 1) + (10 if c > 0 else 0)
        
        return min(ans1, ans2, ans3, ans4)
    
    return dfs(0, 0, 0, 0)

# Input
N, A, B, C = map(int, input().split())
lengths = [int(input()) for _ in range(N)]

# Output
print(min_magic_points(N, A, B, C, lengths))
