
def min_people_to_change_directions(N, S):
    total_people = N
    min_changes = float('inf')
    
    for i in range(N):
        changes = 0
        for j in range(N):
            if i == j:
                continue
            if S[j] == 'W' and (i < j or i > j and S[i] == 'E'):
                changes += 1
        
        if changes < min_changes:
            min_changes = changes
    
    return min_changes

# Read input
N = int(input())
S = input().strip()

# Call the function and print the result
print(min_people_to_change_directions(N, S))
