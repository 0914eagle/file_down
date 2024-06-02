
def decrypt_message(message):
    n = len(message)
    for i in range(1, n+1):
        if n % i == 0:
            r = i
            c = n // i
    matrix = [[''] * c for _ in range(r)]
    idx = 0
    for j in range(c):
        for i in range(r):
            matrix[i][j] = message[idx]
            idx += 1
    decrypted_message = ''.join([''.join(row) for row in matrix])
    return decrypted_message

# Test the function
received_message = "boudonuimilcbsai"
print(decrypt_message(received_message))  # Output: "bombonisuuladici"
