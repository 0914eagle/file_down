
def kth_largest_common_divisor(A, B, K):
    divisors = [i for i in range(1, min(A, B) + 1) if A % i == 0 and B % i == 0]
    sorted_divisors = sorted(divisors, reverse=True)
    return sorted_divisors[K - 1]

# Input
A, B, K = map(int, input().split())

# Output
print(kth_largest_common_divisor(A, B, K))
