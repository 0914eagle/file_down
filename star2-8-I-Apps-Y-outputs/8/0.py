
import string
def get_table(key):
    key = key.replace(' ', '')
    table = {}
    for c in string.ascii_lowercase:
        if c not in key and c != 'q':
            key += c
    i = 0
    for r in range(5):
        for c in range(5):
            table[(r, c)] = key[i]
            i += 1
    return table
def get_coordinates(table, c):
    for r in range(5):
        for c in range(5):
            if table[(r, c)] == c:
                return (r, c)
def get_new_coordinates(r1, c1, r2, c2):
    if r1 == r2:
        return (r1, (c1 + 1) % 5), (r2, (c2 + 1) % 5)
    elif c1 == c2:
        return ((r1 + 1) % 5, c1), ((r2 + 1) % 5, c2)
    return (r1, c2), (r2, c1)
def encrypt(table, text):
    text = text.replace(' ', '')
    text = ''.join([text[i:i+2] for i in range(0, len(text), 2)])
    if len(text) % 2 == 1:
        text += 'x'
    result = ''
    for i in range(0, len(text), 2):
        r1, c1 = get_coordinates(table, text[i])
        r2, c2 = get_coordinates(table, text[i+1])
        r1, r2 = get_new_coordinates(r1, c1, r2, c2)
        result += table[(r1, c1)] + table[(r2, c2)]
    return result.upper()
key = input()
text = input()
table = get_table(key)
print(encrypt(table, text))

