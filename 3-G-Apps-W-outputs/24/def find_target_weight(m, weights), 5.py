
def find_target_weight(m, weights):
    total_weight = sum(weights)
    target_weight = total_weight // 2 + 1
    while True:
        count_lighter = sum(1 for w in weights if w < target_weight)
        count_equal = sum(1 for w in weights if w == target_weight)
        if count_equal % 2 == 0:
            return target_weight
        else:
            target_weight += 1

# Read input
m = int(input())
weights = [int(input()) for _ in range(m)]

# Find and output the smallest integer target weight
target_weight = find_target_weight(m, weights)
print(target_weight)
