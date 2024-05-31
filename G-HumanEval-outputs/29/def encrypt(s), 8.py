
def encrypt(s):
    result = ''
    for char in s:
        if char.isalpha():
            shift = ord(char) - ord('a') + 2
            new_char = chr((shift * 2) % 26 + ord('a'))
            result += new_char
        else:
            result += char
    return result

# Test cases
print(encrypt('hi'))  # 'lm'
print(encrypt('asdfghjkl'))  # 'ewhjklnop'
print(encrypt('gf'))  # 'kj'
print(encrypt('et'))  # 'ix'
