nce_scale(A, B, C, D):
    left_weight = A + B
    right_weight = C + D
    
    if left_weight > right_weight:
        print("Left")
    elif left_weight == right_weight:
        print("Balanced")
    else:
        print("Right")

# Input
input_values = input().split()
A = int(input_values[0])
B = int(input_values[1])
C = int(input_values[2])
D = int(input_values[3])

# Call the function
balance_scale(A, B, C, D)
[/PYTHON