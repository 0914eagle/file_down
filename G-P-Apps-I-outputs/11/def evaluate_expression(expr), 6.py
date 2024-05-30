
variables = {}

def evaluate_expression(expr):
    if '"' in expr:  # String literal
        return expr.strip('"')
    elif '`' in expr:  # Template literal
        parts = expr.split('${')
        result = parts[0]
        for part in parts[1:]:
            var_name = part.split('}')[0]
            result += str(variables[var_name])
            result += part.split('}')[1]
        return result
    else:  # Variable name
        return variables[expr]

while True:
    line = input().strip()
    if line == 'end.':
        break

    if line.startswith('var'):
        parts = line.split('=')
        var_name = parts[0].strip().split(' ')[1]
        var_value = parts[1].strip()
        variables[var_name] = evaluate_expression(var_value)
    elif line.startswith('print'):
        expr = line.split(' ')[1][:-1]
        print(evaluate_expression(expr))
```

