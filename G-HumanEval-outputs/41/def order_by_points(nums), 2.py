
def order_by_points(nums):
    # Define a helper function to calculate the sum of digits for a given number
    def sum_of_digits(n):
        return sum(int(d) for d in str(abs(n)))

    # Sort the list of integers based on the sum of their digits and then by their index
    return sorted(nums, key=lambda x: (sum_of_digits(x), nums.index(x)))

# Test cases
print(order_by_points([1, 11, -1, -11, -12]))  # Output: [-1, -11, 1, -12, 11]
print(order_by_points([]))  # Output: []
