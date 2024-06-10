
s = input()

def insert_plus(s):
    if len(s) == 1:
        return [s]
    
    result = []
    
    for i in range(len(s)):
        for sub in insert_plus(s[:i] + s[i+1:]):
            result.append(s[i] + '+' + sub)
            result.append(s[i] + sub)
    
    return result

formulas = insert_plus(s)

result = 0
for f in formulas:
    result += eval(f)
    
print(result)

