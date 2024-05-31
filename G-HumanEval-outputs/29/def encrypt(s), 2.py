
def encrypt(s):
    encrypted = ""
    for char in s:
        if char.isalpha():
            new_char_code = ord(char) + 2 * 2
            if char.islower():
                if new_char_code > ord('z'):
                    new_char_code -= 26
            elif char.isupper():
                if new_char_code > ord('Z'):
                    new_char_code -= 26
            encrypted += chr(new_char_code)
        else:
            encrypted += char
    return encrypted

# Test cases
print(encrypt('hi')) # Output: 'lm'
print(encrypt('asdfghjkl')) # Output: 'ewhjklnop'
print(encrypt('gf')) # Output: 'kj'
print(encrypt('et')) # Output: 'ix'
