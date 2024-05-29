
def count_nums(arr):
    def sum_digits(n):
        return sum(int(i) for i in str(abs(n)))

    count = 0
    for num in arr:
        if num != 0 and sum_digits(num) > 0:
            count += 1

    return count
