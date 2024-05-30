
def min_explosions(N, A, B, healths):
    def explosion_count(health):
        if health % A == 0:
            return health // A
        else:
            return health // A + 1
    
    total_explosions = 0
    for health in healths:
        total_explosions += explosion_count(health)
    
    return total_explosions

# Sample Input
N, A, B = map(int, input().split())
healths = [int(input()) for _ in range(N)]

# Call the function with the sample input
result = min_explosions(N, A, B, healths)
print(result)
```
