
from string import ascii_lowercase


def playfair(key, text):
    key = "".join(c for c in key if c != "q")
    table = [c for c in key]
    for c in ascii_lowercase:
        if c not in table and c != "q":
            table.append(c)
    def find_pos(c):
        for i in range(len(table)):
            if table[i] == c:
                return i // 5, i % 5
    def process_pair(p):
        if p[0] == p[1]:
            return "x" + p[0]
        r0, c0 = find_pos(p[0])
        r1, c1 = find_pos(p[1])
        if r0 == r1:
            return table[r0 * 5 + (c0 + 1) % 5] + table[r1 * 5 + (c1 + 1) % 5]
        elif c0 == c1:
            return table[(r0 + 1) % 5 * 5 + c0] + table[(r1 + 1) % 5 * 5 + c1]
        return table[r0 * 5 + c1] + table[r1 * 5 + c0]
    pairs = []
    i = 0
    while i < len(text):
        if text[i] == "x" and i < len(text) - 1 and text[i + 1] == "x":
            pairs.append("x")
            i += 1
        elif text[i] == "x" and i == len(text) - 1:
            pairs.append("x")
        else:
            pairs.append(text[i] + text[i + 1])
        i += 2
    encrypted = "".join(process_pair(p) for p in pairs)
    return encrypted.upper()


key = input().strip()
text = input().strip()
print(playfair(key, text))


