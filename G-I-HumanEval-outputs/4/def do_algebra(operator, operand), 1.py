
def do_algebra(operator, operand):
    expr = str(operand[0])
    for i in range(len(operator)):
        expr = expr + operator[i] + str(operand[i + 1])
    return eval(expr)

# Test the function
operators = ['+', '*', '-']
operands = [2, 3, 4, 5]
result = do_algebra(operators, operands)
print("Result:", result)
