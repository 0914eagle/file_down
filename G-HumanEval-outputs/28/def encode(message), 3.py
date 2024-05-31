
def encode(message):
    encoded_message = ""
    vowels = "aeiouAEIOU"
    
    for char in message:
        if char.isalpha():
            if char.lower() in vowels:
                if char.islower():
                    encoded_message += chr((ord(char) - ord('a') + 2) % 26 + ord('A'))
                else:
                    encoded_message += chr((ord(char) - ord('A') + 2) % 26 + ord('A'))
            else:
                if char.islower():
                    encoded_message += char.upper()
                else:
                    encoded_message += char.lower()
        else:
            encoded_message += char
    
    return encoded_message

# Test cases
print(encode('test'))  # Output: 'TGST'
print(encode('This is a message'))  # Output: 'tHKS KS C MGSSCGG'
