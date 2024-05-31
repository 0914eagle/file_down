
def max_additional_sweets(m, k, a, b):
    total_sweets = sum(a)
    eaten_sweets = [0] * m
    for sweet_type in b:
        eaten_sweets[sweet_type - 1] += 1
    
    n = sum(eaten_sweets)
    max_additional = float('inf')
    
    for i in range(m):
        target = a[i] / total_sweets
        lower_bound = n * target - eaten_sweets[i] - 1
        upper_bound = n * target - eaten_sweets[i] + 1
        
        if lower_bound > 0:
            max_additional = min(max_additional, lower_bound)
        if upper_bound < 0:
            return 0
    
    if max_additional == float('inf'):
        return "forever"
    else:
        return max_additional

# Input parsing
m, k = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

result = max_additional_sweets(m, k, a, b)
print(result)
