
def max_boxing_team(n, weights):
    weights_set = set(weights)
    max_team = len(weights_set)
    
    for weight in weights:
        if weight - 1 not in weights_set:
            max_team = max(max_team, len(weights_set) + 1)
        elif weight + 1 not in weights_set:
            max_team = max(max_team, len(weights_set) - 1)
    
    return max_team

# Input
n = int(input())
weights = list(map(int, input().split()))

# Output
print(max_boxing_team(n, weights))
