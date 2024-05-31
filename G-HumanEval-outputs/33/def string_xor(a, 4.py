
def string_xor(a: str, b: str) -> str:
    result = ''
    for char1, char2 in zip(a, b):
        if char1 != char2:
            result += '1'
        else:
            result += '0'
    return result

# Test the function
print(string_xor('010', '110'))  # Output should be '100'
