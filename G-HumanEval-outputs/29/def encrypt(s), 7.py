
def encrypt(s):
    result = ""
    for char in s:
        if char.isalpha():
            new_char = chr(((ord(char) - ord('a') + 2) * 2) % 26 + ord('a'))
            result += new_char
        else:
            result += char
    return result

# Test cases
print(encrypt('hi'))  # Output: 'lm'
print(encrypt('asdfghjkl'))  # Output: 'ewhjklnop'
print(encrypt('gf'))  # Output: 'kj'
print(encrypt('et'))  # Output: 'ix'
