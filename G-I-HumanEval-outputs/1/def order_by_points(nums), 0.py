
def order_by_points(nums):
    def sum_of_digits(num):
        return sum(int(digit) for digit in str(abs(num)))

    nums.sort(key=lambda x: (sum_of_digits(x), nums.index(x)))
    return nums

print(order_by_points([1, 11, -1, -11, -12]))  # Output: [-1, -11, 1, -12, 11]
print(order_by_points([]))  # Output: []

