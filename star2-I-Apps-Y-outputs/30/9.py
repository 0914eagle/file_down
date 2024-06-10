
S = input()
def insert_plus(s, pos):
    return s[:pos] + '+' + s[pos:]
def eval_formula(s):
    return eval(s)
def solve(s):
    if '+' not in s:
        return eval_formula(s)
    else:
        pos = s.index('+')
        return solve(insert_plus(s, pos + 1)) + solve(insert_plus(s, pos + 2))
print(solve(S))

