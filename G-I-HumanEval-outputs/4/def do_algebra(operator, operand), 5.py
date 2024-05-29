
def do_algebra(operator, operand):
    if len(operator) != len(operand) - 1:  # Check if the input is valid
        return "Invalid input"

    expression = str(operand[0])
    for i in range(len(operator)):
        expression += " " + operator[i] + " " + str(operand[i+1])

    return eval(expression)

operator = ['+', '*', '-']
operand = [2, 3, 4, 5]
result = do_algebra(operator, operand)
print(result)
