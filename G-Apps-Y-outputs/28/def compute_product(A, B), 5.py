
def compute_product(A, B):
    product = int(A * float(B))
    return product

# Read input
A, B = map(str, input().split())

# Convert B to a float by dividing by 100
B = float(int(B.replace(".", "")) / 100)

# Call the function and print the result
result = compute_product(int(A), B)
print(result)
