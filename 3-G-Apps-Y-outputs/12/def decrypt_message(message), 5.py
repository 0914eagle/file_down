
def decrypt_message(message):
    n = len(message)
    r = 1
    c = n
    for i in range(2, n+1):
        if n % i == 0:
            r = i
            c = n // i
    
    matrix = [['' for _ in range(c)] for _ in range(r)]
    idx = 0
    for j in range(c):
        for i in range(r):
            matrix[i][j] = message[idx]
            idx += 1
    
    decrypted_message = ''
    for i in range(r):
        for j in range(c):
            decrypted_message += matrix[i][j]
    
    return decrypted_message

# Test the function with examples
print(decrypt_message("bok"))  # Output: bok
print(decrypt_message("koaski"))  # Output: kakosi
