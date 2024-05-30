
import re

variables = {}

def evaluate_expression(expression):
    if expression[0] == '"':
        return expression[1:-1]
    elif expression[0] == '`':
        embedded_expressions = re.findall(r'\${(.*?)}', expression)
        for ex in embedded_expressions:
            expression = expression.replace(f'${{{ex}}}', variables.get(ex, ""))
        return expression[1:-1]

while True:
    command = input()
    if command == 'end.':
        break

    if command.startswith('var'):
        _, name, value = command.split(' = ')
        variables[name] = evaluate_expression(value)
    elif command.startswith('print'):
        _, expression = command.split(" ", 1)
        print(evaluate_expression(expression))

```
