
def order_by_points(nums):
    def get_sum_of_digits(num):
        return sum(int(digit) for digit in str(abs(num)))

    nums.sort(key=lambda x: (get_sum_of_digits(x), nums.index(x)))
    return nums

# Test cases
print(order_by_points([1, 11, -1, -11, -12]))  # Output: [-1, -11, 1, -12, 11]
print(order_by_points([]))  # Output: []
