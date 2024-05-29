
def encrypt(s):
    result = ''
    for char in s:
        if char.isalpha():
            rotated = ord(char) + 2 * 2
            if char.islower():
                if rotated > ord('z'):
                    result += chr(ord('a') + rotated - ord('z') - 1)
                else:
                    result += chr(rotated)
            else:
                if rotated > ord('Z'):
                    result += chr(ord('A') + rotated - ord('Z') - 1)
                else:
                    result += chr(rotated)
        else:
            result += char
    return result

print(encrypt('hi'))  # 'lm'
print(encrypt('asdfghjkl'))  # 'ewhjklnop'
print(encrypt('gf'))  # 'kj'
print(encrypt('et'))  # 'ix'
