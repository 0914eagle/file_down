
def int_to_mini_roman(number):
    if not 1 <= number <= 1000:
        raise ValueError("Input number must be between 1 and 1000")
    
    roman_numerals = {
        1: 'i', 4: 'iv', 5: 'v', 9: 'ix', 10: 'x',
        40: 'xl', 50: 'l', 90: 'xc', 100: 'c',
        400: 'cd', 500: 'd', 900: 'cm', 1000: 'm'
    }
    
    result = ''
    for value, numeral in sorted(roman_numerals.items(), key=lambda x: x[0], reverse=True):
        while number >= value:
            result += numeral
            number -= value

    return result.lower()

# Test cases
assert int_to_mini_roman(19) == 'xix'
assert int_to_mini_roman(152) == 'clii'
assert int_to_mini_roman(426) == 'cdxxvi'
