
def insert_addition_operations(equation):
    A, S = equation.split('=')
    A = A.lstrip('0')  # Remove leading zeros from A
    S = int(S)
    
    for i in range(1, len(A)):
        num1 = int(A[:i])
        remaining = A[i:]
        
        for j in range(1, len(remaining)):
            num2 = int(remaining[:j])
            num3 = int(remaining[j:])
            
            if num1 + num2 + num3 == S:
                corrected_equation = A[:i] + '+' + remaining[:j] + '+' + remaining[j:] + '=' + str(S)
                return corrected_equation

# Input
equation = input().strip()

# Output
print(insert_addition_operations(equation))
