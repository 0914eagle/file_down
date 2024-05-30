
import re

variables = {}

def evaluate_expression(expression):
    if expression in variables:
        return variables[expression]
    
    if '"' in expression:
        return expression.strip('"')
    
    if '`' in expression:
        inner_expr = re.findall(r'\${(.*?)}', expression)
        for exp in inner_expr:
            expression = expression.replace(f'${{{exp}}}', evaluate_expression(exp))
        return expression.strip('`')

def declare_variable(name, value):
    variables[name] = evaluate_expression(value)

def print_expression(expression):
    print(evaluate_expression(expression))

while True:
    command = input().strip()
    if command == 'end.':
        break
    
    if command.startswith('var'):
        _, name, _, value, _ = command.split()
        declare_variable(name, value)
    elif command.startswith('print'):
        _, expression = command.split()
        print_expression(expression)
```
