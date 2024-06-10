
from sys import stdin

def Playfair(key, text):
    table = []
    for c in key:
        if c not in table and c != 'q':
            table.append(c)
    for c in 'abcdefghijklmnopqrstuvwxyz':
        if c not in table and c != 'q':
            table.append(c)
    table = [table[i:i+5] for i in range(0, len(table), 5)]
    text = ''.join([c for c in text if c != ' '])
    pairs = [text[i:i+2] for i in range(0, len(text), 2)]
    if len(text) % 2 == 1:
        pairs.append(text[-1] + 'x')
    def encrypt_pair(pair):
        row1, col1 = divmod(table[0].index(pair[0]), 5)
        row2, col2 = divmod(table[0].index(pair[1]), 5)
        if row1 == row2:
            return table[row1][(col1+1)%5] + table[row2][(col2+1)%5]
        elif col1 == col2:
            return table[(row1+1)%5][col1] + table[(row2+1)%5][col2]
        else:
            return table[row1][col2] + table[row2][col1]
    return ''.join([encrypt_pair(pair) for pair in pairs]).upper()

key = stdin.readline().strip()
text = stdin.readline().strip()
print(Playfair(key, text))

