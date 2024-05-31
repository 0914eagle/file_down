
def do_algebra(operator, operand):
    expression = str(operand[0])
    for i in range(1, len(operand)):
        expression += " " + operator[i-1] + " " + str(operand[i])
    return eval(expression)

# Test the function
operators = ['+', '*', '-']
operands = [2, 3, 4, 5]
result = do_algebra(operators, operands)
print(result)
