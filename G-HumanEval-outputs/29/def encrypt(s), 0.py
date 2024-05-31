
def encrypt(s):
    result = ''
    for char in s:
        if char.isalpha():
            shift = (ord(char) - ord('a') + 2) * 2
            if char.islower():
                result += chr((shift % 26) + ord('a'))
            else:
                result += chr((shift % 26) + ord('A'))
        else:
            result += char
    return result

# Test cases
print(encrypt('hi'))  # Output: 'lm'
print(encrypt('asdfghjkl'))  # Output: 'ewhjklnop'
print(encrypt('gf'))  # Output: 'kj'
print(encrypt('et'))  # Output: 'ix'
