
S = input()

def insert_plus(s, pos):
    return s[:pos] + '+' + s[pos:]

def eval_formula(s):
    return eval(s)

def solve(s):
    if '+' not in s:
        return eval_formula(s)
    
    res = 0
    for i in range(len(s)):
        if s[i] == '+':
            continue
        
        res += solve(insert_plus(s, i))
        
    return res

print(solve(S))

