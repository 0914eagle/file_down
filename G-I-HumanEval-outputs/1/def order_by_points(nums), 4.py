
def order_by_points(nums):
    return sorted(nums, key=lambda x: (sum(int(d) for d in str(abs(x))), nums.index(x)))

# Test cases
print(order_by_points([1, 11, -1, -11, -12]))  # Output: [-1, -11, 1, -12, 11]
print(order_by_points([]))  # Output: []
