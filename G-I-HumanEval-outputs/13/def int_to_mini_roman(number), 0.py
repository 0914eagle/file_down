
def int_to_mini_roman(number):
    if number <= 0 or number > 1000:
        raise ValueError("Input number must be between 1 and 1000")

    values = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
    symbols = ["m", "cm", "d", "cd", "c", "xc", "l", "xl", "x", "ix", "v", "iv", "i"]
    result = ""
    for i in range(len(values)):
        while number >= values[i]:
            result += symbols[i]
            number -= values[i]
    return result.lower()

# Test cases
assert int_to_mini_roman(19) == 'xix'
assert int_to_mini_roman(152) == 'clii'
assert int_to_mini_roman(426) == 'cdxxvi'
