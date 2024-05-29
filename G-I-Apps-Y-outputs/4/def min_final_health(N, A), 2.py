
def min_final_health(N, A):
    # Calculate the greatest common divisor of all initial health values
    def gcd(a, b):
        while b:
            a, b = b, a % b
        return a
    
    initial_gcd = A[0]
    for i in range(1, N):
        initial_gcd = gcd(initial_gcd, A[i])
    
    # The final health of the last monster will be the gcd of the initial health values
    print(initial_gcd)

# Read input
N = int(input())
A = list(map(int, input().split()))

# Call the function with the input values
min_final_health(N, A)
