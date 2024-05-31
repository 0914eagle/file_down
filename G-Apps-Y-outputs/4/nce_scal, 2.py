nce_scale(A, B, C, D):
    left_weight = A + B
    right_weight = C + D
    
    if left_weight > right_weight:
        print("Left")
    elif left_weight == right_weight:
        print("Balanced")
    else:
        print("Right")

# Input processing
input_values = input().split()
A, B, C, D = map(int, input_values)

# Calling the function
balance_scale(A, B, C, D)
[/PYTHON