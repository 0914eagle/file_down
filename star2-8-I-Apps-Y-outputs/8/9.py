
import string
def playfair(key, plaintext):
    table = [c for c in key if c != 'q']
    for c in string.ascii_lowercase:
        if c not in table:
            table.append(c)
    table = [table[i:i+5] for i in range(0, len(table), 5)]
    result = ""
    for i in range(0, len(plaintext), 2):
        a, b = plaintext[i], plaintext[i+1]
        if a == b:
            b = 'x'
        a_row, a_col = -1, -1
        b_row, b_col = -1, -1
        for row in range(5):
            for col in range(5):
                if table[row][col] == a:
                    a_row, a_col = row, col
                if table[row][col] == b:
                    b_row, b_col = row, col
        if a_row == b_row and a_col == b_col:
            result += table[a_row][(a_col+1)%5] + table[b_row][(b_col+1)%5]
        elif a_row == b_row:
            result += table[a_row][(a_col+1)%5] + table[b_row][(b_col+1)%5]
        elif a_col == b_col:
            result += table[(a_row+1)%5][a_col] + table[(b_row+1)%5][b_col]
        else:
            result += table[a_row][b_col] + table[b_row][a_col]
    return result.upper()
key = input()
plaintext = input()
print(playfair(key, plaintext))

