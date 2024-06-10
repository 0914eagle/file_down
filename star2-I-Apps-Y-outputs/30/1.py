
s = input()

def insert_plus(s, pos):
    if pos == len(s):
        return [s]
    else:
        return insert_plus(s[:pos] + '+' + s[pos:], pos + 2) + insert_plus(s, pos + 1)

formulas = insert_plus(s, 1)
print(sum(eval(f) for f in formulas))

