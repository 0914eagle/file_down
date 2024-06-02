
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
                return f"{A[:i]}+{remaining[:j]}+{remaining[j:]}={S}"

# Input
equation = "5025=30"
# Output
print(insert_addition_operations(equation))
