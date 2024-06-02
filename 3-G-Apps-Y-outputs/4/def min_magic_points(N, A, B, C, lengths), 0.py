
def min_magic_points(N, A, B, C, lengths):
    def dfs(a, b, c, idx):
        if idx == N:
            return abs(a - A) + abs(b - B) + abs(c - C) - 30 if min(a, b, c) > 0 else float('inf')
        
        cost1 = dfs(a, b, c, idx + 1)
        cost2 = dfs(a + lengths[idx], b, c, idx + 1) + 10
        cost3 = dfs(a, b + lengths[idx], c, idx + 1) + 10
        cost4 = dfs(a, b, c + lengths[idx], idx + 1) + 10
        cost5 = dfs(a + lengths[idx], b + lengths[idx], c, idx + 1) + 20
        cost6 = dfs(a + lengths[idx], b, c + lengths[idx], idx + 1) + 20
        cost7 = dfs(a, b + lengths[idx], c + lengths[idx], idx + 1) + 20
        cost8 = dfs(a + lengths[idx], b + lengths[idx], c + lengths[idx], idx + 1) + 30
        
        return min(cost1, cost2, cost3, cost4, cost5, cost6, cost7, cost8)
    
    return dfs(0, 0, 0, 0)

# Input processing
input_data = input().split()
N = int(input_data[0])
A = int(input_data[1])
B = int(input_data[2])
C = int(input_data[3])
lengths = [int(input()) for _ in range(N)]

# Call the function and print the result
result = min_magic_points(N, A, B, C, lengths)
print(result)
