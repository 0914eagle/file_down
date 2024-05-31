
def max_additional_sweets(m, k, a, b):
    total_sweets = sum(a)
    eaten_sweets = [0] * m
    for sweet_type in b:
        eaten_sweets[sweet_type - 1] += 1

    target_sum = sum(a) * sum(a[i] / total_sweets for i in range(m))
    remaining_sweets = target_sum * (k + 1) - sum(eaten_sweets)
    if remaining_sweets <= 0:
        return "forever"
    return remaining_sweets

# Input
m, k = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

# Output
print(max_additional_sweets(m, k, a, b))
