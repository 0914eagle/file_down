
def encrypt(s):
    encrypted = ''
    for char in s:
        if char.isalpha():
            shifted = chr(((ord(char) - ord('a') + 2 * 2) % 26) + ord('a'))
            encrypted += shifted
        else:
            encrypted += char
    return encrypted

# Test cases
print(encrypt('hi'))  # Returns 'lm'
print(encrypt('asdfghjkl'))  # Returns 'ewhjklnop'
print(encrypt('gf'))  # Returns 'kj'
print(encrypt('et'))  # Returns 'ix'

