
def balance_scale(A, B, C, D):
    left_weight = A + B
    right_weight = C + D
    
    if left_weight > right_weight:
        return "Left"
    elif left_weight < right_weight:
        return "Right"
    else:
        return "Balanced"

# Input parsing
input_values = list(map(int, input().split()))
A, B, C, D = input_values

result = balance_scale(A, B, C, D)
print(result)
