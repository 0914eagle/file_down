
def max_operations(n, m, array, pairs):
    def gcd(a, b):
        while b:
            a, b = b, a % b
        return a

    def check_divisible(a, b):
        if a % b == 0 or b % a == 0:
            return True
        return False

    max_operations = 0
    for i in range(m):
        ai, aj = pairs[i]
        common_divisor = gcd(array[ai-1], array[aj-1])
        while check_divisible(array[ai-1], common_divisor) and check_divisible(array[aj-1], common_divisor):
            array[ai-1] //= common_divisor
            array[aj-1] //= common_divisor
            max_operations += 1

    return max_operations

# Input parsing
n, m = map(int, input().split())
array = list(map(int, input().split()))
pairs = [list(map(int, input().split())) for _ in range(m)]

# Call the function
result = max_operations(n, m, array, pairs)
print(result)
