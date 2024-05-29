
def int_to_mini_roman(number):
    if not 1 <= number <= 1000:
        return "Number out of range"
    
    roman_nums = {
        1000: 'm', 900: 'cm', 500: 'd', 400: 'cd',
        100: 'c', 90: 'xc', 50: 'l', 40: 'xl',
        10: 'x', 9: 'ix', 5: 'v', 4: 'iv', 1: 'i'
    }
    
    result = ''
    for value, numeral in roman_nums.items():
        while number >= value:
            result += numeral
            number -= value
            
    return result.lower()

# Test cases
print(int_to_mini_roman(19))  # Output: 'xix'
print(int_to_mini_roman(152))  # Output: 'clii'
print(int_to_mini_roman(426))  # Output: 'cdxxvi'
