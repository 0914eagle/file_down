
def string_xor(a: str, b: str) -> str:
    result = ''
    for i in range(len(a)):
        result += str(int(a[i]) ^ int(b[i]))
    return result

print(string_xor('010', '110'))  # Output: '100'
