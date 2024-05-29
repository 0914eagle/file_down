
def do_algebra(operator, operand):
    operators = {
        '+': lambda x, y: x + y,
        '-': lambda x, y: x - y,
        '*': lambda x, y: x * y,
        '//': lambda x, y: x // y,
        '**': lambda x, y: x ** y
    }
    
    result = operand[0]
    for i in range(len(operator)):
        result = operators[operator[i]](result, operand[i + 1])
    
    return result

# Test the function
operators = ['+', '*', '-']
operands = [2, 3, 4, 5]
print(do_algebra(operators, operands))  # Output: 9
