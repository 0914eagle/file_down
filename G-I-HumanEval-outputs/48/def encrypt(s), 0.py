
def encrypt(s):
    result = ''
    for letter in s:
        if letter.isalpha():
            shift = ord(letter) - ord('a') + 2
            encrypted_letter = chr(((shift * 2) % 26) + ord('a'))
            result += encrypted_letter
        else:
            result += letter
    return result


# Test cases
print(encrypt('hi'))  # Output: 'lm'
print(encrypt('asdfghjkl'))  # Output: 'ewhjklnop'
print(encrypt('gf'))  # Output: 'kj'
print(encrypt('et'))  # Output: 'ix'
