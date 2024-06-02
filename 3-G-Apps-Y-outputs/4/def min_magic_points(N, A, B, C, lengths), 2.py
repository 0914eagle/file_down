
def min_magic_points(N, A, B, C, lengths):
    lengths.sort(reverse=True)
    
    def dfs(idx, a, b, c):
        if idx == N:
            if a == A and b == B and c == C:
                return 0
            else:
                return float('inf')
        
        mp1 = dfs(idx + 1, a, b, c)
        mp2 = float('inf')
        mp3 = float('inf')
        
        if a < A:
            mp2 = 1 + dfs(idx + 1, a + 1, b, c)
        
        if b < B and lengths[idx] != b:
            mp3 = 10 + dfs(idx + 1, a, b + lengths[idx], c)
        
        return min(mp1, mp2, mp3)
    
    return dfs(0, 0, 0, 0)

# Input
N, A, B, C = map(int, input().split())
lengths = [int(input()) for _ in range(N)]

# Output
print(min_magic_points(N, A, B, C, lengths))
