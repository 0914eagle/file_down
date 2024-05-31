
def kth_largest_divisor(A, B, K):
    divisors = []
    for i in range(1, min(A, B) + 1):
        if A % i == 0 and B % i == 0:
            divisors.append(i)
    
    divisors.sort(reverse=True)
    return divisors[K - 1]

# Read input from standard input
A, B, K = map(int, input().split())
print(kth_largest_divisor(A, B, K))
