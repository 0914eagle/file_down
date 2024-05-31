
def encrypt(s):
    result = ""
    for char in s:
        if char.isalpha():
            ascii_val = ord(char)
            shifted_val = ascii_val + 2 * 2
            if char.islower():
                if shifted_val > ord('z'):
                    shifted_val -= 26
            elif char.isupper():
                if shifted_val > ord('Z'):
                    shifted_val -= 26
            result += chr(shifted_val)
        else:
            result += char
    return result

# Test cases
print(encrypt('hi'))  # Output: 'lm'
print(encrypt('asdfghjkl'))  # Output: 'ewhjklnop'
print(encrypt('gf'))  # Output: 'kj'
print(encrypt('et'))  # Output: 'ix'
