
def find_target_weight(m, weights):
    total_weight = sum(weights)
    target_weight = total_weight // 2 + 1
    animals_equal_to_target = sum(1 for w in weights if w == target_weight)
    
    if animals_equal_to_target % 2 == 0:
        return target_weight
    else:
        return target_weight + 1

# Input
m = int(input())
weights = [int(input()) for _ in range(m)]

# Output
print(find_target_weight(m, weights))
