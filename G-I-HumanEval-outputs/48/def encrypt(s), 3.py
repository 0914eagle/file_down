
def encrypt(s):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    result = ''

    for char in s:
        if char.isalpha():
            shifted_index = (alphabet.index(char) + (2 * 2)) % len(alphabet)
            result += alphabet[shifted_index]
        else:
            result += char

    return result

# Test cases
print(encrypt('hi'))  # 'lm'
print(encrypt('asdfghjkl'))  # 'ewhjklnop'
print(encrypt('gf'))  # 'kj'
print(encrypt('et'))  # 'ix'
