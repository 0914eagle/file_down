
def find_minimum_amount(N, K, disliked_digits):
    while True:
        if all(str(digit) not in str(N) for digit in disliked_digits):
            return N
        N += 1

# Read input
N, K = map(int, input().split())
disliked_digits = list(map(int, input().split()))

result = find_minimum_amount(N, K, disliked_digits)
print(result)
```
