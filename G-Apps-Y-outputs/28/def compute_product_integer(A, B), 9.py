
def compute_product_integer(A, B):
    product = A * float(B)
    product_integer = int(product)
    print(product_integer)

# Read input from Standard Input
A, B = input().split()
A = int(A)
B = float(B)

compute_product_integer(A, B)
