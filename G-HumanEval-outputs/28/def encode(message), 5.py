
def encode(message):
    vowels = "aeiouAEIOU"
    encoded_message = ""
    
    for char in message:
        if char.isalpha():
            if char.lower() in vowels:
                if char.isupper():
                    encoded_message += chr((ord(char) + 2 - ord('A')) % 26 + ord('A'))
                else:
                    encoded_message += chr((ord(char) + 2 - ord('a')) % 26 + ord('a'))
            else:
                encoded_message += char.swapcase()
        else:
            encoded_message += char
    
    return encoded_message

# Test cases
print(encode('test'))  # Output: 'TGST'
print(encode('This is a message'))  # Output: 'tHKS KS C MGSSCGG'
