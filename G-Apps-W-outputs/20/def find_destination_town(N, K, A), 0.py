
def find_destination_town(N, K, A):
    visited = [False] * N
    current_town = 0
    visited[current_town] = True

    cycle_start_town = None
    cycle_length = 0

    while K > 0:
        K -= 1
        current_town = A[current_town] - 1
        if visited[current_town]:
            cycle_start_town = current_town
            break
        visited[current_town] = True

    if cycle_start_town is not None:
        cycle_length = 1
        current_town = A[current_town] - 1
        while current_town != cycle_start_town:
            cycle_length += 1
            current_town = A[current_town] - 1

    remaining_steps = K % cycle_length if cycle_length > 0 else 1
    current_town = 0

    for _ in range(remaining_steps):
        current_town = A[current_town] - 1

    return current_town + 1

# Read input
N, K = map(int, input().split())
A = list(map(int, input().split()))

# Call the function and print the output
print(find_destination_town(N, K, A))
