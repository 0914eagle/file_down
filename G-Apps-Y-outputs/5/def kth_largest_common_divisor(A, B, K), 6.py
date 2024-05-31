
def kth_largest_common_divisor(A, B, K):
    common_divisors = []
    for i in range(1, min(A, B) + 1):
        if A % i == 0 and B % i == 0:
            common_divisors.append(i)
    
    common_divisors.sort(reverse=True)
    return common_divisors[K - 1]

# Reading input from Standard Input
A, B, K = map(int, input().split())

# Calling the function and printing the result
result = kth_largest_common_divisor(A, B, K)
print(result)
