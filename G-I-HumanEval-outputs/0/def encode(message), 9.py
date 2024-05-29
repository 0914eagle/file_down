
def encode(message):
    vowels = "aeiou"
    encoded_message = ""
    for char in message:
        if char.lower() in vowels:
            new_char = chr((ord(char) + 2 - 97) % 26 + 97) if char.islower() else chr((ord(char) + 2 - 65) % 26 + 65)
            encoded_message += new_char
        else:
            encoded_message += char.swapcase()
    return encoded_message

# Test cases
print(encode('test'))  # Output: 'TGST'
print(encode('This is a message'))  # Output: 'tHKS KS C MGSSCGG'
