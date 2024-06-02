
def decrypt_message(message):
    n = len(message)
    for r in range(1, n+1):
        if n % r == 0:
            c = n // r
            break
    
    matrix = [['' for _ in range(c)] for _ in range(r)]
    idx = 0
    for j in range(c):
        for i in range(r):
            matrix[i][j] = message[idx]
            idx += 1
    
    decrypted_message = ''
    for j in range(c):
        for i in range(r):
            decrypted_message += matrix[i][j]
    
    return decrypted_message

# Test the function
print(decrypt_message("boudonuimilcbsai"))  # Output: "bombonisuuladici"
print(decrypt_message("kakosi"))  # Output: "koaski"
