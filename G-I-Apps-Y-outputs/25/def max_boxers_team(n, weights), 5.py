
def max_boxers_team(n, weights):
    unique_weights = set(weights)
    
    max_team_size = len(unique_weights)
    for weight in unique_weights:
        if weight - 1 not in unique_weights:
            max_team_size += 1
        elif weight + 1 not in unique_weights:
            max_team_size += 1
    
    return max_team_size

# Reading input
n = int(input())
weights = list(map(int, input().split()))

# Calling the function and printing the result
print(max_boxers_team(n, weights))
