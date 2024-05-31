
def compute_product(A, B):
    result = int(A * float(B))
    print(result)

# Read input from Standard Input
A, B = input().split()
A = int(A)
B = float(B)

compute_product(A, B)
