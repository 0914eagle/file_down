
def max_operations(n, m, arr, pairs):
    def gcd(a, b):
        while b:
            a, b = b, a % b
        return a

    ans = 0
    for i, j in pairs:
        divisor = gcd(arr[i-1], arr[j-1])
        while divisor != 1:
            arr[i-1] //= divisor
            arr[j-1] //= divisor
            ans += 1
            divisor = gcd(arr[i-1], arr[j-1])
    
    return ans

# Input
n, m = map(int, input().split())
arr = list(map(int, input().split()))
pairs = [tuple(map(int, input().split())) for _ in range(m)]

# Output
print(max_operations(n, m, arr, pairs))
