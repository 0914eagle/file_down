
def balanced_sweets(m, k, a, b):
    total_sweets = sum(a)
    eaten_sweets = [0] * m
    for sweet_type in b:
        eaten_sweets[sweet_type - 1] += 1

    remaining_sweets = total_sweets - k
    target_sweets = [round(f * remaining_sweets) for f in a]

    min_additional_sweets = float('inf')
    for i in range(m):
        min_additional_sweets = min(min_additional_sweets, max(target_sweets[i] - eaten_sweets[i], 0))

    if min_additional_sweets == 0:
        return "forever"
    else:
        return min_additional_sweets

# Input
m, k = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

# Output
print(balanced_sweets(m, k, a, b))
