
import re

variables = {}

def evaluate_expression(expr):
    if expr in variables:
        return variables[expr]
    elif expr.startswith('"') and expr.endswith('"'):
        return expr[1:-1]
    else:
        matches = re.findall(r'\${(.*?)}', expr)
        for match in matches:
            expr = expr.replace(f'${{{match}}}', evaluate_expression(match))
        return expr

while True:
    command = input().strip()
    
    if command == 'end.':
        break
    
    if command.startswith('var'):
        _, name, value = command.split(' = ')
        value = value.rstrip(';')
        variables[name] = evaluate_expression(value)
    elif command.startswith('print'):
        _, expr = command.split(' ')
        expr = expr.rstrip(';')
        print(evaluate_expression(expr))
```

