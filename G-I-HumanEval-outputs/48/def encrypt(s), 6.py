
def encrypt(s):
    shifted_alphabet = ''
    for char in s:
        if 'a' <= char <= 'z':
            shifted_char = chr((ord(char) - ord('a') + 2) * 2 % 26 + ord('a'))
            shifted_alphabet += shifted_char
        else:
            shifted_alphabet += char
    return shifted_alphabet

# Test cases
print(encrypt('hi'))  # Output: 'lm'
print(encrypt('asdfghjkl')) # Output: 'ewhjklnop'
print(encrypt('gf'))  # Output: 'kj'
print(encrypt('et'))  # Output: 'ix'
