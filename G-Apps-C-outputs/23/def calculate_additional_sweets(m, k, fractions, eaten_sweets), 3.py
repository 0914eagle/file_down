
def calculate_additional_sweets(m, k, fractions, eaten_sweets):
    total_sweets = sum(eaten_sweets)
    target_sweets = [fraction * total_sweets for fraction in fractions]
    
    remaining_sweets = [0] * m
    for sweet_type in eaten_sweets:
        remaining_sweets[sweet_type - 1] += 1
    
    max_additional_sweets = float('inf')
    for i in range(m):
        deficit = target_sweets[i] - remaining_sweets[i]
        if deficit > 0:
            max_additional_sweets = min(max_additional_sweets, deficit)
    
    if max_additional_sweets == float('inf'):
        return "forever"
    else:
        return max_additional_sweets

# Read input
m, k = map(int, input().split())
fractions = list(map(int, input().split()))
eaten_sweets = list(map(int, input().split()))

# Calculate and print result
result = calculate_additional_sweets(m, k, fractions, eaten_sweets)
print(result)
