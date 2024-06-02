
def min_magic_points(N, A, B, C, bamboos):
    def dfs(a, b, c, idx):
        if idx == N:
            return abs(a - A) + abs(b - B) + abs(c - C) - 30
        cost1 = dfs(a, b, c, idx + 1)
        cost2 = dfs(a + bamboos[idx], b, c, idx + 1) + 10
        cost3 = dfs(a, b + bamboos[idx], c, idx + 1) + 10
        cost4 = dfs(a, b, c + bamboos[idx], idx + 1) + 10
        return min(cost1, cost2, cost3, cost4)
    
    return dfs(0, 0, 0, 0)

# Input processing
input_data = input().split()
N = int(input_data[0])
A = int(input_data[1])
B = int(input_data[2])
C = int(input_data[3])
bamboos = [int(input()) for _ in range(N)]

# Calculate and print the minimum amount of MP needed
print(min_magic_points(N, A, B, C, bamboos))
