
# Define a dictionary to store variable values
variables = {}

# Function to evaluate expression
def evaluate_expression(expression):
    if expression in variables:
        return variables[expression]
    elif expression.startswith('"') and expression.endswith('"'):
        return expression[1:-1]
    elif expression.startswith('`') and expression.endswith('`'):
        parts = expression[1:-1].split('${')
        result = parts[0]
        for part in parts[1:]:
            var_name, remaining = part.split('}', 1)
            result += evaluate_expression(var_name) + remaining
        return result

# Read input commands
while True:
    command = input()
    if command == 'end.':
        break
    elif command.startswith('var'):
        parts = command.split('=')
        var_name = parts[0].strip().split()[1]
        expression = parts[1].strip().rstrip(';')
        variables[var_name] = evaluate_expression(expression)
    elif command.startswith('print'):
        expression = command.split()[1]
        print(evaluate_expression(expression))

```
