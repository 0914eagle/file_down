
def calculate_cuts(K, N, poles):
    total_len = sum(poles)
    min_cut = total_len // N
    return max(0, N - K - min_cut)

# Input
input_str = input().strip()
K, N = map(int, input_str.split())
poles = list(map(int, input().strip().split()))

# Output
print(calculate_cuts(K, N, poles))
```
