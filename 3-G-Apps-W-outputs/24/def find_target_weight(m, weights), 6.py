
def find_target_weight(m, weights):
    total_weight = sum(weights)
    target_weight = total_weight // 2
    animals_equal_to_target = [weight for weight in weights if weight == target_weight]
    
    if len(animals_equal_to_target) % 2 == 0:
        return target_weight
    else:
        return target_weight + 1

# Input processing
m = int(input())
weights = [int(input()) for _ in range(m)]

# Output
print(find_target_weight(m, weights))
