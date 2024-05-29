
def count_nums(arr):
    def sum_of_digits(num):
        sum_digits = 0
        negative = False

        if num < 0:
            negative = True
            num = abs(num)

        while num > 0:
            digit = num % 10
            sum_digits += digit
            num //= 10

        return -sum_digits if negative else sum_digits

    count = 0
    for num in arr:
        if sum_of_digits(num) > 0:
            count += 1

    return count

# Test cases
print(count_nums([]) == 0)
print(count_nums([-1, 11, -11]) == 1)
print(count_nums([1, 1, 2]) == 3)
