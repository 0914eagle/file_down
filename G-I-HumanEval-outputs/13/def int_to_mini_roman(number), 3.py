
def int_to_mini_roman(number):
    if not isinstance(number, int) or not 1 <= number <= 1000:
        return "Input out of range."
    
    val_list = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
    roman_list = ["m", "cm", "d", "cd", "c", "xc", "l", "xl", "x", "ix", "v", "iv", "i"]
    
    result = ''
    for i in range(len(val_list)):
        while number >= val_list[i]:
            result += roman_list[i]
            number -= val_list[i]
    
    return result.lower()

# Test cases
print(int_to_mini_roman(19))  # Output: xix
print(int_to_mini_roman(152))  # Output: clii
print(int_to_mini_roman(426))  # Output: cdxxvi
print(int_to_mini_roman(1001))  # Output: Input out of range.
