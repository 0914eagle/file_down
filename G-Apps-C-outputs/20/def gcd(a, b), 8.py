
def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)

def count_common_factors(arr):
    n = len(arr)
    count = 0
    for i in range(n):
        factors = set()
        for j in range(n):
            if i != j:
                factors.add(gcd(arr[i], arr[j]))
        if len(factors) > 0:
            count += 1
    return pow(2, count-1, 10**9 + 7)

n = int(input())
numbers = [int(input()) for _ in range(n)]
result = count_common_factors(numbers)
print(result)
