
from string import ascii_lowercase

def playfair(key, message):
    table = [[""] * 5 for _ in range(5)]
    alphabet = ascii_lowercase.replace("q", "")
    i, j = 0, 0
    for c in key:
        if c not in alphabet:
            continue
        alphabet = alphabet.replace(c, "")
        table[i][j] = c
        j += 1
        if j >= 5:
            j = 0
            i += 1
    for c in alphabet:
        table[i][j] = c
        j += 1
        if j >= 5:
            j = 0
            i += 1
    encrypted = ""
    i = 0
    while i < len(message):
        c1, c2 = message[i], message[i+1]
        if c1 == c2:
            c2 = "x"
        r1, c1 = divmod(alphabet.index(c1), 5)
        r2, c2 = divmod(alphabet.index(c2), 5)
        if r1 == r2:
            encrypted += table[r1][(c1+1)%5] + table[r2][(c2+1)%5]
        elif c1 == c2:
            encrypted += table[(r1+1)%5][c1] + table[(r2+1)%5][c2]
        else:
            encrypted += table[r1][c2] + table[r2][c1]
        i += 2

    return encrypted.upper()

