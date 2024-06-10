
def find_perfect_integer(k):
    number_of_digits = 1
    count = 0
    while count < k:
        sum_of_digits = 0
        number_of_digits += 1
        for digit in str(number_of_digits):
            sum_of_digits += int(digit)
        if sum_of_digits == 10:
            count += 1
    return number_of_digits

k = int(input())
print(find_perfect_integer(k))

