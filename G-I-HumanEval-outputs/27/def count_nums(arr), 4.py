
def count_nums(arr):
    def sum_of_digits(num):
        if num < 0:
            num *= -1
        return sum(int(digit) for digit in str(num))

    count = 0
    for num in arr:
        if sum_of_digits(num) > 0:
            count += 1

    return count

# Test cases
assert count_nums([]) == 0
assert count_nums([-1, 11, -11]) == 1
assert count_nums([1, 1, 2]) == 3

print("All test cases passed!")
