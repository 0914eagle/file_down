
def decrease_number(n, k):
    for _ in range(k):
        if n % 10 == 0:
            n //= 10
        else:
            n -= 1
    return n

# Input
n, k = map(int, input().split())

# Output
result = decrease_number(n, k)
print(result)
