
def max_additional_sweets(m, k, a, b):
    total_sweets = sum(a)
    target_fractions = [ai / total_sweets for ai in a]
    
    sweets_count = [0] * m
    for bi in b:
        sweets_count[bi - 1] += 1
    
    min_allowed_sweets = [int(k * f - 1) for f in target_fractions]
    max_allowed_sweets = [int(k * f + 1) for f in target_fractions]
    
    additional_sweets = float('inf')
    for i in range(m):
        additional_sweets = min(additional_sweets, max(0, max_allowed_sweets[i] - sweets_count[i]))
    
    if additional_sweets == float('inf'):
        return "forever"
    else:
        return additional_sweets

# Input
m, k = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

# Output
result = max_additional_sweets(m, k, a, b)
print(result)
