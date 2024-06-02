
def find_target_weight(weights):
    total_weight = sum(weights)
    target_weight = total_weight // 2 + 1
    return target_weight

# Read input
m = int(input())
weights = [int(input()) for _ in range(m)]

# Find and output the smallest target weight
print(find_target_weight(weights))
