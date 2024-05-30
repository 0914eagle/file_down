
variables = {}

def evaluate_expression(expression):
    if expression[0] == '"' and expression[-1] == '"':
        return expression[1:-1]
    elif expression[0] == '`' and expression[-1] == '`':
        parts = expression[1:-1].split('${')
        result = ""
        for part in parts:
            if '}' in part:
                var_name = part.split('}')[0]
                result += evaluate_expression(variables.get(var_name, ''))
                result += part.split('}')[1]
            else:
                result += part
        return result
    else:
        return variables.get(expression, '')

while True:
    line = input().strip()
    if line == 'end.':
        break
    if line.startswith('var'):
        parts = line.split('=')
        var_name = parts[0].split()[-1].strip()
        var_value = parts[1].strip().strip(';')
        variables[var_name] = var_value
    elif line.startswith('print'):
        expr = line.split(None, 1)[1].strip().strip(';')
        print(evaluate_expression(expr))
```
