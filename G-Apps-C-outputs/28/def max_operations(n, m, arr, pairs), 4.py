
def max_operations(n, m, arr, pairs):
    operations = 0
    
    for i, j in pairs:
        while arr[i-1] % 2 == 0 and arr[j-1] % 2 == 0:
            arr[i-1] //= 2
            arr[j-1] //= 2
            operations += 1
    
    return operations

# Input parsing
n, m = map(int, input().split())
arr = list(map(int, input().split()))
pairs = [tuple(map(int, input().split())) for _ in range(m)]

result = max_operations(n, m, arr, pairs)
print(result)
