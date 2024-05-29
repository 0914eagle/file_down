
def encrypt(s):
    encrypted = ''
    for char in s:
        if char.isalpha():
            base = ord('a') if char.islower() else ord('A')
            encrypted += chr((ord(char) - base + 2 * 2) % 26 + base)
        else:
            encrypted += char
    return encrypted

# Test cases
print(encrypt('hi'))        # Output: 'lm'
print(encrypt('asdfghjkl')) # Output: 'ewhjklnop'
print(encrypt('gf'))        # Output: 'kj'
print(encrypt('et'))        # Output: 'ix'
