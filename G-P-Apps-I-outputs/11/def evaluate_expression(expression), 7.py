
import re

variables = {}

def evaluate_expression(expression):
    if '"' in expression:
        return expression.strip('"')
    elif '`' in expression:
        expr_parts = re.split(r'\${(.*?)}', expression)
        evaluated_parts = [evaluate_expression(part) if i % 2 == 1 else part for i, part in enumerate(expr_parts)]
        return ''.join(evaluated_parts)
    else:
        return variables.get(expression)

cmd = input()
while cmd != 'end.':
    if cmd.startswith('var'):
        _, name, _, value, _ = cmd.split()
        variables[name] = evaluate_expression(value)
    elif cmd.startswith('print'):
        _, expr = cmd.split()
        print(evaluate_expression(expr.strip(';')))
    
    cmd = input()

