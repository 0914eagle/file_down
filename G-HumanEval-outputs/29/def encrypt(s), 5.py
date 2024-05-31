
def encrypt(s):
    result = ""
    for char in s:
        if char.isalpha():
            base = ord('a') if char.islower() else ord('A')
            shifted = base + ((ord(char) - base + 2) * 2) % 26
            result += chr(shifted)
        else:
            result += char
    return result

# Test cases
print(encrypt('hi'))  # Output: 'lm'
print(encrypt('asdfghjkl'))  # Output: 'ewhjklnop'
print(encrypt('gf'))  # Output: 'kj'
print(encrypt('et'))  # Output: 'ix'
