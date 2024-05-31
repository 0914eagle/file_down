
def sweets_balance(m, k, a, b):
    total_sweets = sum(a)
    current_sweets = [0] * m
    for sweet_type in b:
        current_sweets[sweet_type - 1] += 1

    remaining_sweets = total_sweets - k
    remaining_balance = []
    for i in range(m):
        target_sweets = total_sweets * a[i] / sum(a)
        min_sweets = target_sweets - current_sweets[i]
        max_sweets = total_sweets * a[i] / sum(a) + 1 - current_sweets[i]
        remaining_balance.append((min_sweets, max_sweets))

    min_additional_sweets = max(0, min([x[0] for x in remaining_balance]))
    max_additional_sweets = min(remaining_sweets, min([x[1] for x in remaining_balance]))

    if min_additional_sweets <= max_additional_sweets:
        return max_additional_sweets
    else:
        return "forever"

# Input
m, k = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

# Output
print(sweets_balance(m, k, a, b))
