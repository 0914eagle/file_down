
def insert_addition_operations(equation):
    A, S = equation.split('=')
    A = A.lstrip('0')
    S = int(S)
    
    for i in range(1, len(A)):
        num1 = int(A[:i])
        remaining = A[i:]
        for j in range(1, len(remaining)):
            num2 = int(remaining[:j])
            num3 = int(remaining[j:])
            if num1 + num2 + num3 == S:
                return f"{str(num1)}+{str(num2)}+{str(num3)}={str(S)}"
    
    return None

equation = input().strip()
result = insert_addition_operations(equation)
print(result)
