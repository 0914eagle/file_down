
def do_algebra(operator, operand):
    if len(operator) != len(operand) - 1:
        return "Error: Length of operator list must be one less than length of operand list."
    
    result = operand[0]
    for i in range(len(operator)):
        if operator[i] == '+':
            result += operand[i + 1]
        elif operator[i] == '-':
            result -= operand[i + 1]
        elif operator[i] == '*':
            result *= operand[i + 1]
        elif operator[i] == '//':
            result //= operand[i + 1]
        elif operator[i] == '**':
            result **= operand[i + 1]
    
    return result

# Test the function
operators = ['+', '*', '-']
operands = [2, 3, 4, 5]
print(do_algebra(operators, operands))  # Output should be 9
