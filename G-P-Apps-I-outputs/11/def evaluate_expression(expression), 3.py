
variables = {}

def evaluate_expression(expression):
    if isinstance(expression, str):
        return expression
    elif isinstance(expression, list):
        return ''.join([evaluate_expression(expr) for expr in expression])

def process_command(command):
    if command.startswith('var'):
        parts = command.split(' = ')
        var_name = parts[0][4:]
        expression = parts[1][parts[1].index('=') + 2:-1]
        if expression.startswith('`'):
            expression = expression[1:-1].split('${')
            expression = [part.split('}') for part in expression]
            variables[var_name] = evaluate_expression(expression)
        else:
            variables[var_name] = expression
    elif command.startswith('print'):
        expr = command[6:-1]
        print(evaluate_expression(expr))

while True:
    command = input()
    if command == 'end.':
        break
    process_command(command)
