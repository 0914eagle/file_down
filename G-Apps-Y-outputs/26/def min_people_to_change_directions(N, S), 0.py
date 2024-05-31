
def min_people_to_change_directions(N, S):
    prefix_sum_E = [0] * (N + 1)
    prefix_sum_W = [0] * (N + 1)
    
    for i in range(1, N + 1):
        prefix_sum_E[i] = prefix_sum_E[i - 1] + (S[i - 1] == 'E')
        prefix_sum_W[i] = prefix_sum_W[i - 1] + (S[i - 1] == 'W')
    
    min_changes = float('inf')
    for i in range(1, N + 1):
        west_changes = prefix_sum_E[i - 1]
        east_changes = prefix_sum_W[N] - prefix_sum_W[i]
        total_changes = west_changes + east_changes
        min_changes = min(min_changes, total_changes)
    
    return min_changes

# Read input
N = int(input())
S = input().strip()

# Call the function with input values
result = min_people_to_change_directions(N, S)
print(result)
