
def odd_digit_num(n):
    return sum(9 * 10 ** i for i in range(len(str(n))))

