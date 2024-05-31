
def truncate_multiplication(A, B):
    result = int(A * float(B))
    print(result)

# Taking input
A, B = input().split()
A = int(A)
B = float(B)

# Calling the function
truncate_multiplication(A, B)
