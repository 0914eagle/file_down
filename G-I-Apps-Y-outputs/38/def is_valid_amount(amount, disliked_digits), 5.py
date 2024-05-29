
def is_valid_amount(amount, disliked_digits):
    while amount > 0:
        if amount % 10 in disliked_digits:
            return False
        amount //= 10
    return True

def find_minimum_amount(N, K, disliked_digits):
    while not is_valid_amount(N, disliked_digits):
        N += 1
    return N

# Read input
N, K = map(int, input().split())
disliked_digits = list(map(int, input().split()))

# Find and output the minimum amount
print(find_minimum_amount(N, K, disliked_digits))
```
