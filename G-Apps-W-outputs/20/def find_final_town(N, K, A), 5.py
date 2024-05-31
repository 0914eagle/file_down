
def find_final_town(N, K, A):
    visited = [False] * N
    current_town = 0
    visited[0] = True
    cycle_start = 0
    cycle_length = 0

    for _ in range(K):
        current_town = A[current_town] - 1
        if visited[current_town]:
            cycle_start = current_town
            break
        visited[current_town] = True
        cycle_length += 1

    if cycle_length == 0:
        return current_town + 1

    remaining_steps = (K - cycle_start) % cycle_length
    for _ in range(remaining_steps):
        current_town = A[current_town] - 1

    return current_town + 1

# Read input from Standard Input
N, K = map(int, input().split())
A = list(map(int, input().split()))

# Call the function and print the result
print(find_final_town(N, K, A))
