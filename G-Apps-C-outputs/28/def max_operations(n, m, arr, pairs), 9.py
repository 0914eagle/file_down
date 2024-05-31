
def max_operations(n, m, arr, pairs):
    def gcd(a, b):
        while b:
            a, b = b, a % b
        return a

    def can_divide(a, b):
        g = gcd(a, b)
        while g != 1:
            a //= g
            g = gcd(a, b)
        return a == 1

    operations = 0

    for i, j in pairs:
        if can_divide(arr[i-1], arr[j-1]):
            operations += 1

    return operations

# Input
n, m = map(int, input().split())
arr = list(map(int, input().split()))
pairs = [tuple(map(int, input().split())) for _ in range(m)]

# Output
print(max_operations(n, m, arr, pairs))
