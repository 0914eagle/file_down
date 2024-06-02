
def find_flavor(N, L):
    total_flavor = L * N + N * (N - 1) // 2
    return total_flavor - min(abs(L), N)

# Input
N, L = map(int, input().split())

# Output
print(find_flavor(N, L))
