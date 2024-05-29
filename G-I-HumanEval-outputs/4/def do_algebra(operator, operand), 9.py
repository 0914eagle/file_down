
def do_algebra(operator, operand):
    if len(operator) != len(operand) - 1:
        raise ValueError("Invalid input. Operator list length should be one less than operand list length.")

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
        else:
            raise ValueError("Invalid operator. Supported operators are '+', '-', '*', '//', and '**'.")

    return result

# Testing the function
operator = ['+', '*', '-']
operand = [2, 3, 4, 5]
print(do_algebra(operator, operand))  # Output should be 9
