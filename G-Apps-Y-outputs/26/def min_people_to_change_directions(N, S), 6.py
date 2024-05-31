
def min_people_to_change_directions(N, S):
    west_count = S.count('W')
    east_count = S.count('E')

    min_changes = float('inf')
    current_changes = 0
    for i in range(N):
        if i < west_count:
            if S[i] == 'E':
                current_changes += 1
        else:
            if S[i] == 'W':
                current_changes += 1
        min_changes = min(min_changes, current_changes)

    return min_changes

# Read input
N = int(input())
S = input().strip()

# Call the function and print the result
result = min_people_to_change_directions(N, S)
print(result)
