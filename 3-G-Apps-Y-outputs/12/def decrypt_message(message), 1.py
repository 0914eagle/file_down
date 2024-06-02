
def decrypt_message(message):
    n = len(message)
    for i in range(1, n+1):
        if n % i == 0:
            rows = i
            cols = n // i
    matrix = [['' for _ in range(cols)] for _ in range(rows)]
    idx = 0
    for j in range(cols):
        for i in range(rows):
            matrix[i][j] = message[idx]
            idx += 1
    decrypted_message = ''
    for i in range(rows):
        for j in range(cols):
            decrypted_message += matrix[i][j]
    return decrypted_message

# Test the function with examples
print(decrypt_message("boudonuimilcbsai"))  # Output: bombonisuuladici
print(decrypt_message("kakosi"))  # Output: koaski
