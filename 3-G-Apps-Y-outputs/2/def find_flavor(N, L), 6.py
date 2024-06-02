
def find_flavor(N, L):
    total_flavor = 0
    min_diff = float('inf')
    for i in range(1, N+1):
        flavor = L + i - 1
        total_flavor += flavor
        if abs(flavor) < abs(min_diff):
            min_diff = flavor
    return total_flavor - min_diff

# Input
N, L = map(int, input().split())

# Output
print(find_flavor(N, L))
