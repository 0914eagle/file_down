
def balance_scale(A, B, C, D):
    left_weight = A + B
    right_weight = C + D
    
    if left_weight > right_weight:
        return "Left"
    elif left_weight == right_weight:
        return "Balanced"
    else:
        return "Right"

# Input processing
input_values = input().split()
A, B, C, D = map(int, input_values)

# Output
print(balance_scale(A, B, C, D))
