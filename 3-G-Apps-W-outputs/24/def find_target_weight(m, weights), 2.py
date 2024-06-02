
def find_target_weight(m, weights):
    total_weight = sum(weights)
    half_weight = total_weight // 2
    sorted_weights = sorted(weights)
    
    cumulative_sum = 0
    target_weight = 0
    for weight in sorted_weights:
        cumulative_sum += weight
        if cumulative_sum >= half_weight:
            target_weight = weight
            break
    
    return target_weight

# Input
m = int(input())
weights = []
for _ in range(m):
    weights.append(int(input()))

# Output
print(find_target_weight(m, weights))
