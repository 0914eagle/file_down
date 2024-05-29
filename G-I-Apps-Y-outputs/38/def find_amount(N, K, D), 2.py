
def find_amount(N, K, D):
    while True:
        str_N = str(N)
        if all(d not in str_N for d in D):
            return N
        N += 1

# Read input from standard input
N, K = map(int, input().split())
D = list(map(int, input().split()))

result = find_amount(N, K, D)
print(result)
```
