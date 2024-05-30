
variables = {}

def evaluate_expression(expr):
    if '"' in expr:
        return expr.strip('"')
    elif '`' in expr:
        expr = expr.strip('`')
        parts = expr.split('${')
        result = ''
        for part in parts:
            if '}' in part:
                var_name = part.split('}')[0]
                if var_name in variables:
                    result += variables[var_name]
                result += part.split('}')[1]
            else:
                result += part
        return result
    else:
        return variables[expr]

while True:
    command = input().strip()
    if command == 'end.':
        break
    elif command.startswith('var'):
        parts = command.split('=')
        var_name = parts[0].split()[1].strip()
        var_value = parts[1].strip(';').strip()
        variables[var_name] = evaluate_expression(var_value)
    elif command.startswith('print'):
        expr = command.split()[1].strip(';').strip()
        print(evaluate_expression(expr))
```

