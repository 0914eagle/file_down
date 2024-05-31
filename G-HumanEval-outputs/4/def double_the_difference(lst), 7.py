
def double_the_difference(lst):
    total = 0
    for num in lst:
        if num > 0 and num % 2 != 0 and isinstance(num, int):
            total += num ** 2
    return total * 2
