
def int_to_mini_roman(number):
    if number < 1 or number > 1000:
        raise ValueError("Number must be between 1 and 1000 inclusive")

    roman_nums = {
        1: 'i', 4: 'iv', 5: 'v', 9: 'ix', 10: 'x', 40: 'xl', 50: 'l',
        90: 'xc', 100: 'c', 400: 'cd', 500: 'd', 900: 'cm', 1000: 'm'
    }

    result = ''
    for value, numeral in sorted(roman_nums.items(), reverse=True):
        while number >= value:
            result += numeral
            number -= value

    return result.lower()

# Test cases
print(int_to_mini_roman(19) == 'xix')
print(int_to_mini_roman(152) == 'clii')
print(int_to_mini_roman(426) == 'cdxxvi')
