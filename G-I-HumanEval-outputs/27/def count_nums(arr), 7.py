
def count_nums(arr):
    def get_digits_sum(num):
        if num < 0:
            num = -num
        digits_sum = 0
        while num > 0:
            digits_sum += num % 10
            num //= 10
        return digits_sum

    count = 0
    for num in arr:
        if get_digits_sum(num) > 0:
            count += 1
    return count

# Test cases
print(count_nums([]))    # 0
print(count_nums([-1, 11, -11]))    # 1
print(count_nums([1, 1, 2]))    # 3
