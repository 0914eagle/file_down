
def encrypt(s):
    result = ''
    for char in s:
        if char.isalpha():
            shift = ord(char) + 2 * 2
            if char.islower():
                if shift > ord('z'):
                    shift -= 26
            elif char.isupper():
                if shift > ord('Z'):
                    shift -= 26
            result += chr(shift)
        else:
            result += char
    return result

# Test cases
print(encrypt('hi'))  # 'lm'
print(encrypt('asdfghjkl'))  # 'ewhjklnop'
print(encrypt('gf'))  # 'kj'
print(encrypt('et'))  # 'ix'
