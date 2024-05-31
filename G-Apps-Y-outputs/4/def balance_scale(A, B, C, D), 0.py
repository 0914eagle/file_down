
def balance_scale(A, B, C, D):
    left_weight = A + B
    right_weight = C + D

    if left_weight > right_weight:
        return "Left"
    elif left_weight == right_weight:
        return "Balanced"
    else:
        return "Right"

# Read input from Standard Input
A, B, C, D = map(int, input().split())

# Call the function and print the result
result = balance_scale(A, B, C, D)
print(result)
