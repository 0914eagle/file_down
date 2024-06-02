
def vigenere_decrypt(encrypted_message, key):
    decrypted_message = ""
    for i in range(len(encrypted_message)):
        shift = ord(key[i]) - ord('A') if i % 2 == 0 else ord('Z') - ord(key[i]) + 1
        decrypted_char = chr((ord(encrypted_message[i]) - ord('A') - shift) % 26 + ord('A'))
        decrypted_message += decrypted_char
    return decrypted_message

# Input
encrypted_message = input().strip()
key = input().strip()

# Decrypt the message
decrypted_message = vigenere_decrypt(encrypted_message, key)
print(decrypted_message)
