
def playfair(key, text):
    table = [[0 for _ in range(5)] for _ in range(5)]
    alpha = [chr(i) for i in range(ord('a'), ord('z') + 1)]
    alpha.remove('q')
    key = [ch for ch in key if ch != ' ']
    for ch in key:
        if ch in alpha:
            alpha.remove(ch)
    for i in range(5):
        for j in range(5):
            if key:
                table[i][j] = key.pop(0)
            else:
                table[i][j] = alpha.pop(0)
    result = ""
    for i in range(0, len(text), 2):
        ch1, ch2 = text[i], text[i + 1]
        if ch1 == ch2:
            text = text[:i + 1] + "x" + text[i + 1:]
            ch2 = "x"
        row1, col1 = -1, -1
        row2, col2 = -1, -1
        for i in range(5):
            for j in range(5):
                if table[i][j] == ch1:
                    row1, col1 = i, j
                if table[i][j] == ch2:
                    row2, col2 = i, j
        if row1 == row2:
            col1 = (col1 + 1) % 5
            col2 = (col2 + 1) % 5
        elif col1 == col2:
            row1 = (row1 + 1) % 5
            row2 = (row2 + 1) % 5
        else:
            col1, col2 = col2, col1
        result += table[row1][col1] + table[row2][col2]
    return result.upper()

