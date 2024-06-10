

def calc_prod(arr):
    arr.sort()
    n = len(arr)
    prod = 1
    for i in range(n-1):
        for j in range(i+1, n):
            prod = (prod * abs(arr[i] - arr[j])) % m
    
    return prod

n, m = map(int, input().split())
arr = list(map(int, input().split()))
print(calc_prod(arr))


