
def calculate_operations(n, m, arr, pairs):
    def gcd(a, b):
        while b:
            a, b = b, a % b
        return a
    
    def max_operations(a, i, j):
        g = gcd(a[i], a[j])
        count = 0
        while g != 1:
            count += 1
            g //= 2
        return count
    
    max_ops = 0
    for i, j in pairs:
        operations = max_operations(arr, i-1, j-1)
        max_ops = max(max_ops, operations)
    
    return max_ops

# Input processing
n, m = map(int, input().split())
arr = list(map(int, input().split()))
pairs = [tuple(map(int, input().split())) for _ in range(m)]

# Output
print(calculate_operations(n, m, arr, pairs))
