
def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def max_operations(n, m, arr, pairs):
    max_ops = 0
    for i, j in pairs:
        gcd_val = gcd(arr[i-1], arr[j-1])
        while gcd_val != 1:
            arr[i-1] //= gcd_val
            arr[j-1] //= gcd_val
            max_ops += 1
            gcd_val = gcd(arr[i-1], arr[j-1])
    return max_ops

# Input
n, m = map(int, input().split())
arr = list(map(int, input().split()))
pairs = [tuple(map(int, input().split())) for _ in range(m)]

# Output
print(max_operations(n, m, arr, pairs))
