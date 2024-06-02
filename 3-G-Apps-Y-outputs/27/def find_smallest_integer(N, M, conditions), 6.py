
def find_smallest_integer(N, M, conditions):
    for i in range(10**(N-1), 10**N):
        if all(str(i)[s-1] == str(c) for s, c in conditions):
            return i
    return -1

# Read input
N, M = map(int, input().split())
conditions = [tuple(map(int, input().split())) for _ in range(M)]

# Find and print the smallest integer
result = find_smallest_integer(N, M, conditions)
print(result)
