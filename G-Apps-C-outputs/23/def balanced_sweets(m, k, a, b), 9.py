
def balanced_sweets(m, k, a, b):
    total_sweets = sum(a)
    s = [0] * m
    for sweet_type in b:
        s[sweet_type - 1] += 1
        
    n = sum(s)
    remaining_sweets = total_sweets * n - n
    max_additional_sweets = total_sweets - n if remaining_sweets == 0 else remaining_sweets // (total_sweets - n)
    
    if max_additional_sweets == 0:
        return "forever"
    else:
        return max_additional_sweets

# Input
m, k = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

# Output
print(balanced_sweets(m, k, a, b))
