
def find_target_weight(m, weights):
    total_weight = sum(weights)
    target_weight = total_weight // 2
    weights.sort()
    
    for weight in weights:
        if weight > target_weight:
            break
        target_weight -= weight
    
    return target_weight

# Input
m = int(input())
weights = []
for _ in range(m):
    weight = int(input())
    weights.append(weight)

# Output
print(find_target_weight(m, weights))
