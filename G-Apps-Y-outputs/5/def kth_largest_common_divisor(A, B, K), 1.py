
def kth_largest_common_divisor(A, B, K):
    divisors = []
    for i in range(1, min(A, B) + 1):
        if A % i == 0 and B % i == 0:
            divisors.append(i)
    
    return divisors[-K]

# Read input from Standard Input
A, B, K = map(int, input().split())

# Call the function and print the result
print(kth_largest_common_divisor(A, B, K))
