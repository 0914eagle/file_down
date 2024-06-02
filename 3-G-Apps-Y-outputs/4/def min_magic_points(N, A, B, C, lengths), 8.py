
def min_magic_points(N, A, B, C, lengths):
    def dfs(idx, a, b, c):
        if idx == N:
            return abs(a - A) + abs(b - B) + abs(c - C) if min(a, b, c) > 0 else float('inf')
        
        res = float('inf')
        res = min(res, dfs(idx + 1, a, b, c))
        res = min(res, 10 + dfs(idx + 1, a + lengths[idx], b, c))
        res = min(res, 10 + dfs(idx + 1, a, b + lengths[idx], c))
        res = min(res, 10 + dfs(idx + 1, a, b, c + lengths[idx]))
        res = min(res, 1 + dfs(idx + 1, a - lengths[idx], b, c))
        res = min(res, 1 + dfs(idx + 1, a, b - lengths[idx], c))
        res = min(res, 1 + dfs(idx + 1, a, b, c - lengths[idx]))
        
        return res
    
    return dfs(0, 0, 0, 0)

# Input processing
input_data = input().strip().split()
N = int(input_data[0])
A = int(input_data[1])
B = int(input_data[2])
C = int(input_data[3])

lengths = []
for _ in range(N):
    lengths.append(int(input().strip()))

result = min_magic_points(N, A, B, C, lengths)
print(result)
