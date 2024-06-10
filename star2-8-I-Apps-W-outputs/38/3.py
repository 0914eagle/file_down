
def max_number_of_offices(n):
    total_numbers = 9 ** n
    lucky_numbers = 0
    for num in range(1, total_numbers + 1):
        digits = list(str(num))
        if all(digit in '78' for digit in digits):
            lucky_numbers += 1
    
    return lucky_numbers

