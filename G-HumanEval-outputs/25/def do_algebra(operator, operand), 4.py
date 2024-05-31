
def do_algebra(operator, operand):
    # Initialize the result with the first operand
    result = operand[0]
    
    # Iterate through the operators and operands to build the expression
    for i in range(len(operator)):
        op = operator[i]
        num = operand[i+1]
        
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
operator = ['+', '*', '-']
operand = [2, 3, 4, 5]
print(do_algebra(operator, operand))  # Output: 9
```
