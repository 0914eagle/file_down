
def compute_product_truncate_fraction(A, B):
    result = int(A * float(B))
    print(result)

# Read input from Standard Input
A, B = map(str, input().split())

# Convert A to an integer
A = int(A)

# Call the function with input values
compute_product_truncate_fraction(A, B)
