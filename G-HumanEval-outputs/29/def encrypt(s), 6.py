
def encrypt(s):
    encrypted = ""
    for char in s:
        if char.isalpha():
            shift = 2 * (ord('z') - ord(char)) + 1
            encrypted += chr(ord('a') + (ord(char) - ord('a') + shift) % 26)
        else:
            encrypted += char
    return encrypted

print(encrypt('hi')) # 'lm'
print(encrypt('asdfghjkl')) # 'ewhjklnop'
print(encrypt('gf')) # 'kj'
print(encrypt('et')) # 'ix'
