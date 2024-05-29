
def count_nums(arr):
    def sum_digits(num):
        if num == 0:
            return 0
        sign = -1 if num < 0 else 1
        num = abs(num)
        total = 0
        while num > 0:
            total += num % 10
            num //= 10
        return total * sign

    count = 0
    for num in arr:
        if sum_digits(num) > 0:
            count += 1

    return count

# Test cases
print(count_nums([]))  # 0
print(count_nums([-1, 11, -11]))  # 1
print(count_nums([1, 1, 2]))  # 3