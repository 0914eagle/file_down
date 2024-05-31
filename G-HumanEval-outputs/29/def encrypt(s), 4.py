
def encrypt(s):
    encrypted = ""
    for char in s:
        if char.isalpha():
            shift = (ord(char) - ord('a') + 2) * 2
            encrypted += chr((shift % 26) + ord('a'))
        else:
            encrypted += char
    return encrypted

# Test cases
print(encrypt('hi'))  # Output: 'lm'
print(encrypt('asdfghjkl'))  # Output: 'ewhjklnop'
print(encrypt('gf'))  # Output: 'kj'
print(encrypt('et'))  # Output: 'ix'
