
def kth_largest_common_divisor(A, B, K):
    common_divisors = []
    
    for i in range(1, min(A, B) + 1):
        if A % i == 0 and B % i == 0:
            common_divisors.append(i)
    
    common_divisors.sort(reverse=True)
    
    return common_divisors[K - 1]

# Read input from Standard Input
A, B, K = map(int, input().split())

# Call the function and print the result
print(kth_largest_common_divisor(A, B, K))
