
def find_flavor(N, L):
    total_flavor = N * L + N * (N - 1) // 2
    min_diff = float('inf')
    for i in range(1, N + 1):
        flavor_without_i = total_flavor - L - i
        diff = abs(total_flavor - 2 * flavor_without_i)
        min_diff = min(min_diff, diff)
    return total_flavor - min_diff

# Read input
N, L = map(int, input().split())

# Call the function and print the result
print(find_flavor(N, L))
