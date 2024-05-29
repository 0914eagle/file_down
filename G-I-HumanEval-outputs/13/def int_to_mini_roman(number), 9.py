
def int_to_mini_roman(number):
    if not isinstance(number, int) or number < 1 or number > 1000:
        return "Invalid input"

    roman_numerals = [
        (1000, 'm'), (900, 'cm'), (500, 'd'), (400, 'cd'),
        (100, 'c'), (90, 'xc'), (50, 'l'), (40, 'xl'),
        (10, 'x'), (9, 'ix'), (5, 'v'), (4, 'iv'), (1, 'i')
    ]

    roman_str = ''
    for value, numeral in roman_numerals:
        while number >= value:
            roman_str += numeral
            number -= value

    return roman_str.lower()

# Test cases
print(int_to_mini_roman(19))  # Output: 'xix'
print(int_to_mini_roman(152))  # Output: 'clii'
print(int_to_mini_roman(426))  # Output: 'cdxxvi'
