
def find_flavor(N, L):
    total_flavor = N * L + N * (N - 1) // 2
    return total_flavor - min(abs(L), N-1)

# Input
N, L = map(int, input().split())

# Output
print(find_flavor(N, L))
