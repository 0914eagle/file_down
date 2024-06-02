
def min_magic_points(N, A, B, C, lengths):
    def dfs(a, b, c, idx):
        if idx == N:
            return abs(a - A) + abs(b - B) + abs(c - C) - 30 if min(a, b, c) > 0 else float('inf')
        
        mp1 = dfs(a, b, c, idx + 1)
        mp2 = dfs(a + lengths[idx], b, c, idx + 1) + 10
        mp3 = dfs(a, b + lengths[idx], c, idx + 1) + 10
        mp4 = dfs(a, b, c + lengths[idx], idx + 1) + 10
        mp5 = dfs(a + lengths[idx], b + lengths[idx], c, idx + 1) + 10
        mp6 = dfs(a + lengths[idx], b, c + lengths[idx], idx + 1) + 10
        mp7 = dfs(a, b + lengths[idx], c + lengths[idx], idx + 1) + 10
        mp8 = dfs(a + lengths[idx], b + lengths[idx], c + lengths[idx], idx + 1) + 10
        
        return min(mp1, mp2, mp3, mp4, mp5, mp6, mp7, mp8)
    
    return dfs(0, 0, 0, 0)

# Input
N, A, B, C = map(int, input().split())
lengths = [int(input()) for _ in range(N)]

# Output
print(min_magic_points(N, A, B, C, lengths))
