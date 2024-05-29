
def encode(message):
    encoded_message = ""
    vowels = "AEIOUaeiou"
    
    for char in message:
        if char.isalpha():
            if char.upper() in vowels:
                encoded_char = chr(ord(char) + 2)
                if encoded_char > 'z':
                    encoded_char = chr(ord(encoded_char) - 26)
                encoded_message += encoded_char
            else:
                if char.islower():
                    encoded_message += char.upper()
                else:
                    encoded_message += char.lower()
        else:
            encoded_message += char
            
    return encoded_message

# Test the function with examples
print(encode('test'))
print(encode('This is a message'))
