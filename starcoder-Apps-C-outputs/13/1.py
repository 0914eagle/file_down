
def gen_table():
    table = {'a': [], 'b': [], 'c': [], 'd': [], 'e': [], 'f': [], 'g': [], 'h': [], 'i': [], 'j': [], 'k': [], 'l': [], 'm': [], 'n': [], 'o': [], 'p': [], 'q': [], 'r': [], 's': [], 't': [], 'u': [], 'v': [], 'w': [], 'x': [], 'y': [], 'z': []}
    for word in ['be', 'our', 'rum', 'will', 'dead', 'hook', 'ship', 'blood', 'sable', 'avenge', 'parrot', 'captain']:
        for c in word:
            if c in table:
                table[c].append(word)
    return table

def find_common(table, c, s):
    word_list = table[c]
    for word in word_list:
        if s.find(word) >= 0:
            return True
    return False

def find_word(table, s):
    for c in s:
        if find_common(table, c, s):
            return True
    return False

def find_cipher(table, s):
    if len(s) > 0:
        c = s[0]
        word_list = table[c]
        for word in word_list:
            if s.find(word) >= 0:
                return word
    return ""

def solve(s):
    if len(s) > 0:
        table = gen_table()
        cipher = find_cipher(table, s)
        if len(cipher) > 0:
            return cipher + " " + solve(s.replace(cipher, "", 1))
    return ""

def main():
    s = input()
    print(solve(s))

if __name__ == "__main__":
    main()
