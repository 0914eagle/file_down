
def compute_product_as_integer(A, B):
    result = int(A * float(B))
    print(result)

# Read input from Standard Input
A, B = input().split()
A = int(A)
B = float(B)

compute_product_as_integer(A, B)
