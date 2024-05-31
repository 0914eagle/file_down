
def compute_product(A, B):
    result = int(A * float(B))
    print(result)

# Input
A, B = input().strip().split()
A = int(A)
B = float(B)

# Compute and output the result
compute_product(A, B)
