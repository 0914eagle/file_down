
def encrypt(s):
    result = ""
    for char in s:
        if char.isalpha():
            shifted = ord(char) + 2 * 2
            if char.islower():
                if shifted > ord('z'):
                    shifted -= 26
            else:
                if shifted > ord('Z'):
                    shifted -= 26
            result += chr(shifted)
        else:
            result += char
    return result

# Test cases
print(encrypt('hi'))  # 'lm'
print(encrypt('asdfghjkl'))  # 'ewhjklnop'
print(encrypt('gf'))  # 'kj'
print(encrypt('et'))  # 'ix'
