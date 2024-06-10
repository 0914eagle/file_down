
import sys
import string

def get_key_table(keyphrase):
    keyphrase = keyphrase.upper()
    keyphrase = keyphrase.replace(" ", "")
    keyphrase = "".join([ch for ch in keyphrase if ch != "Q"])
    table = [ch for ch in keyphrase]
    alphabet = string.ascii_uppercase
    alphabet = alphabet.replace("Q", "")
    for ch in alphabet:
        if ch not in table:
            table.append(ch)
    table = [table[i:i+5] for i in range(0, len(table), 5)]
    return table

def find_position(ch, key_table):
    for i, row in enumerate(key_table):
        if ch in row:
            return i, row.index(ch)
    return None, None

def encrypt_playfair(keyphrase, plaintext):
    key_table = get_key_table(keyphrase)
    plaintext = plaintext.upper()
    plaintext = plaintext.replace(" ", "")
    plaintext = "".join([ch for ch in plaintext if ch != "Q"])
    if len(plaintext) % 2 == 1:
        plaintext += "X"
    ciphertext = ""
    for i in range(0, len(plaintext), 2):
        ch1, ch2 = plaintext[i], plaintext[i+1]
        row1, col1 = find_position(ch1, key_table)
        row2, col2 = find_position(ch2, key_table)
        if row1 == row2:
            ciphertext += key_table[row1][(col1+1)%5] + key_table[row2][(col2+1)%5]
        elif col1 == col2:
            ciphertext += key_table[(row1+1)%5][col1] + key_table[(row2+1)%5][col2]
        else:
            ciphertext += key_table[row1][col2] + key_table[row2][col1]
    return ciphertext

if __name__ == "__main__":
    keyphrase = sys.stdin.readline().strip()
    plaintext = sys.stdin.readline().strip()
    ciphertext = encrypt_playfair(keyphrase, plaintext)
    print(ciphertext)


