
def encrypt(s):
    result = ""
    for char in s:
        if char.isalpha():
            shifted = ord(char) + 2 * 2
            if char.islower():
                if shifted > ord('z'):
                    shifted -= 26
            elif char.isupper():
                if shifted > ord('Z'):
                    shifted -= 26
            result += chr(shifted)
        else:
            result += char
    return result

# Test cases
print(encrypt('hi'))  # Output: 'lm'
print(encrypt('asdfghjkl'))  # Output: 'ewhjklnop'
print(encrypt('gf'))  # Output: 'kj'
print(encrypt('et'))  # Output: 'ix'
