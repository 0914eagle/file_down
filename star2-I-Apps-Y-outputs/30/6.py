
s = input()
result = 0
for i in range(2 ** (len(s) - 1)):
    formula = s[0]
    for j in range(1, len(s)):
        if (i >> (j - 1)) & 1:
            formula += '+'
        formula += s[j]
    result += eval(formula)
print(result)

