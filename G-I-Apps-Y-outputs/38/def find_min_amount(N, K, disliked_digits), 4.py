
def find_min_amount(N, K, disliked_digits):
    N_str = str(N)
    while any(d in N_str for d in disliked_digits):
        N += 1
        N_str = str(N)
    return N

N, K = map(int, input().split())
disliked_digits = list(map(int, input().split()))

result = find_min_amount(N, K, disliked_digits)
print(result)
```
