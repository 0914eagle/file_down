
def read_input():
    key = input()
    text = input()
    return key, text


def fill_key_table(key):
    table = []
    for row in range(5):
        table.append([])
        for col in range(5):
            table[row].append(None)
    key = ''.join(set(key))
    for row in range(5):
        for col in range(5):
            if len(key) > 0:
                table[row][col] = key[0]
                key = key[1:]
            else:
                break

    return table


def find_pos(table, ch):
    for row in range(5):
        for col in range(5):
            if table[row][col] == ch:
                return row, col


def apply_rule(table, ch1, ch2):
    row1, col1 = find_pos(table, ch1)
    row2, col2 = find_pos(table, ch2)
    if ch1 == ch2:
        return 'X' + ch2
    elif row1 == row2:
        return table[row1][(col1 + 1) % 5] + table[row2][(col2 + 1) % 5]
    elif col1 == col2:
        return table[(row1 + 1) % 5][col1] + table[(row2 + 1) % 5][col2]
    else:
        return table[row1][col2] + table[row2][col1]


def encrypt(table, text):
    text = text.replace(' ', '')
    if len(text) % 2 == 1:
        text += 'X'
    encrypted = ''
    for i in range(0, len(text), 2):
        encrypted += apply_rule(table, text[i], text[i + 1])

    return encrypted


def main():
    key, text = read_input()
    table = fill_key_table(key)
    encrypted = encrypt(table, text)
    print(encrypted.upper())


main()

