
def check_coinciding_tracks(n, L, kefa, sasha):
    kefa_shifted = kefa + kefa  # Double the distances to make it easier to check overlapping
    for i in range(n):
        if kefa_shifted[i:i+n] == sasha:
            return "YES"
    return "NO"

# Read input
n, L = map(int, input().split())
kefa = list(map(int, input().split()))
sasha = list(map(int, input().split()))

# Check and print output
coincide = check_coinciding_tracks(n, L, kefa, sasha)
print(coincide)
```
