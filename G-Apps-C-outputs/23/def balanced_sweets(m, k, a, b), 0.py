
def balanced_sweets(m, k, a, b):
    total_sweets = sum(a)
    current_counts = [b.count(i) for i in range(1, m+1)]
    n = sum(current_counts)
    
    for i in range(m):
        lower_bound = n * a[i] - 1
        upper_bound = n * a[i] + 1
        if current_counts[i] < lower_bound:
            additional_sweets = min(upper_bound - current_counts[i], total_sweets - n)
            return additional_sweets
    return "forever"

# Input parsing
m, k = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

print(balanced_sweets(m, k, a, b))
