
def do_algebra(operator, operand):
    expression = str(operand[0])
    for i in range(len(operator)):
        expression += operator[i] + str(operand[i+1])
    return eval(expression)

# Test the function
operators = ['+', '*', '-']
operands = [2, 3, 4, 5]
result = do_algebra(operators, operands)
print(result)
