
def find_target_weight(m, weights):
    total_weight = sum(weights)
    target_weight = total_weight // 2 + 1
    for weight in weights:
        if weight >= target_weight:
            target_weight = weight
            break
    return target_weight

# Read input
m = int(input())
weights = [int(input()) for _ in range(m)]

# Find and output the smallest integer target weight
print(find_target_weight(m, weights))
