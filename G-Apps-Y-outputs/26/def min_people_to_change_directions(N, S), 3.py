
def min_people_to_change_directions(N, S):
    count_W_to_E = [0] * (N + 1)
    count_E_to_W = [0] * (N + 1)
    
    for i in range(1, N + 1):
        count_W_to_E[i] = count_W_to_E[i-1] + (S[i-1] == 'E')
        count_E_to_W[i] = count_E_to_W[i-1] + (S[i-1] == 'W')
    
    min_changes = float('inf')
    for i in range(1, N + 1):
        changes = count_E_to_W[i-1] + (N - i) - count_W_to_E[i]
        min_changes = min(min_changes, changes)
    
    return min_changes

# Input
N = int(input())
S = input().strip()

# Output
print(min_people_to_change_directions(N, S))
