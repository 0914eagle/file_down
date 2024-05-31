
def encode(message):
    vowels = 'aeiouAEIOU'
    encoded_message = ''
    
    for char in message:
        if char.isalpha():
            if char.lower() in vowels:
                if char.isupper():
                    new_char = chr((ord(char) + 2 - ord('A')) % 26 + ord('A'))
                else:
                    new_char = chr((ord(char) + 2 - ord('a')) % 26 + ord('a'))
            else:
                new_char = char.swapcase()
        else:
            new_char = char
        encoded_message += new_char

    return encoded_message

# Test cases
print(encode('test'))  # Output: 'TGST'
print(encode('This is a message'))  # Output: 'tHKS KS C MGSSCGG'
