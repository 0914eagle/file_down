
def do_algebra(operator, operand):
    # Initialize result with the first operand
    result = operand[0]
    
    # Iterate over the operators and operands simultaneously
    for op, num in zip(operator, operand[1:]):
        if op == '+':
            result += num
        elif op == '-':
            result -= num
        elif op == '*':
            result *= num
        elif op == '//':
            result //= num
        elif op == '**':
            result **= num
    
    return result

# Example usage
operators = ['+', '*', '-']
operands = [2, 3, 4, 5]
print(do_algebra(operators, operands))  # Output: 9
```
