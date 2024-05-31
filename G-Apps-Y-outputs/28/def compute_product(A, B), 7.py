
def compute_product(A, B):
    result = int(A * float(B))
    print(result)

# Read input
A, B = map(str, input().split())

# Convert B to a float
B = float(B)

# Call the function
compute_product(int(A), B)
