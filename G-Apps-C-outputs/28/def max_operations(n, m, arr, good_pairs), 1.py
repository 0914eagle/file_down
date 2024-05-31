
def max_operations(n, m, arr, good_pairs):
    def gcd(a, b):
        while b:
            a, b = b, a % b
        return a

    def is_divisible(a, b):
        return a % b == 0

    def max_operations_single_pair(pair, arr):
        i, j = pair
        common_divisor = gcd(arr[i-1], arr[j-1])
        count = 0
        while is_divisible(arr[i-1], common_divisor) and is_divisible(arr[j-1], common_divisor):
            arr[i-1] //= common_divisor
            arr[j-1] //= common_divisor
            count += 1
        return count

    total_operations = 0
    for pair in good_pairs:
        total_operations += max_operations_single_pair(pair, arr)
    return total_operations

# Input parsing
n, m = map(int, input().split())
arr = list(map(int, input().split()))
good_pairs = [tuple(map(int, input().split())) for _ in range(m)]

# Output
print(max_operations(n, m, arr, good_pairs))
