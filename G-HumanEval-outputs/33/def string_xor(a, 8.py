
def string_xor(a: str, b: str) -> str:
    result = ''
    for i in range(len(a)):
        if a[i] != b[i]:
            result += '1'
        else:
            result += '0'
    return result

print(string_xor('010', '110'))  # Output: '100'
