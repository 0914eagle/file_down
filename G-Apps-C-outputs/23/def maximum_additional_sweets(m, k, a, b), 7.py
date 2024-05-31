
def maximum_additional_sweets(m, k, a, b):
    total_sweets = sum(a)
    current_sweets = [0] * m
    for i in range(k):
        current_sweets[b[i] - 1] += 1

    max_additional_sweets = float('inf')
    for i in range(m):
        target_sweets = total_sweets * a[i] / total_sweets
        if current_sweets[i] < target_sweets - 1:
            max_additional_sweets = min(max_additional_sweets, target_sweets - current_sweets[i] - 1)
        elif current_sweets[i] > target_sweets + 1:
            return 0

    if max_additional_sweets == float('inf'):
        return "forever"
    return max_additional_sweets

# Read input
m, k = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

# Call the function and print the result
result = maximum_additional_sweets(m, k, a, b)
print(result)
