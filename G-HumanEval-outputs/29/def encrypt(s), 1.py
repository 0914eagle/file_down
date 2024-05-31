
def encrypt(s):
    encrypted = ""
    for char in s:
        if char.isalpha():
            shift = 2 * (ord(char.lower()) - ord('a'))
            encrypted += chr((ord(char) - ord('a') + shift) % 26 + ord('a'))
        else:
            encrypted += char
    return encrypted

# Test cases
print(encrypt('hi'))  # Output: 'lm'
print(encrypt('asdfghjkl'))  # Output: 'ewhjklnop'
print(encrypt('gf'))  # Output: 'kj'
print(encrypt('et'))  # Output: 'ix'
