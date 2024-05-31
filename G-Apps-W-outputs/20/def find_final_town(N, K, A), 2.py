
def find_final_town(N, K, A):
    visited = [False] * N
    current_town = 0  # Start at Town 1
    visited[current_town] = True
    cycle_start_idx = 0
    cycle_length = 0
    
    for _ in range(K):
        current_town = A[current_town] - 1
        if visited[current_town]:
            cycle_start_idx = A.index(A[current_town])
            cycle_length = _ - cycle_start_idx + 1
            break
        visited[current_town] = True
    
    if cycle_length > 0:
        remaining_steps = (K - cycle_start_idx) % cycle_length
        current_town = 0
        for _ in range(remaining_steps):
            current_town = A[current_town] - 1
    return current_town + 1

# Reading input from Standard Input
N, K = map(int, input().split())
A = list(map(int, input().split()))

# Calling the function to find the final town
result = find_final_town(N, K, A)

# Printing the final town
print(result)
