
def balanced_diet(m, k, a, b):
    total_sweets = sum(b)
    target_fractions = [ai/sum(a) for ai in a]
    current_counts = [b.count(i) for i in range(1, m+1)]

    max_additional_sweets = float("inf")
    for i in range(m):
        min_sweets = max(0, total_sweets * target_fractions[i] - current_counts[i] - 1)
        max_sweets = total_sweets * target_fractions[i] - current_counts[i] + 1
        max_additional_sweets = min(max_additional_sweets, max_sweets)

    if max_additional_sweets == float("inf"):
        return "forever"
    else:
        return max_additional_sweets

# Input
m, k = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

# Output
print(balanced_diet(m, k, a, b))
