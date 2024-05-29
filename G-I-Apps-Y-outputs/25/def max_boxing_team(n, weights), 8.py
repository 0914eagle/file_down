
def max_boxing_team(n, weights):
    weights.sort()
    unique_weights = set()
    
    for weight in weights:
        if weight not in unique_weights:
            unique_weights.add(weight)
        elif weight - 1 not in unique_weights:
            unique_weights.add(weight - 1)
        else:
            unique_weights.add(weight + 1)
    
    return len(unique_weights)

# Input parsing
n = int(input())
weights = list(map(int, input().split()))

# Call the function and print the result
print(max_boxing_team(n, weights))
