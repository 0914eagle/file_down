
def find_teleporter_destination(N, K, A):
    visited = [False] * N
    current_town = 0
    visited[current_town] = True
    cycle_start = 0
    cycle_length = 0

    while True:
        current_town = A[current_town] - 1
        if visited[current_town]:
            cycle_start = current_town
            break
        visited[current_town] = True

    cycle_length = 1
    next_town = A[current_town] - 1
    while next_town != current_town:
        cycle_length += 1
        next_town = A[next_town] - 1

    remaining_steps = K
    current_town = 0
    while remaining_steps > 0:
        if remaining_steps >= cycle_length:
            remaining_steps -= cycle_length
            current_town = cycle_start
        else:
            current_town = A[current_town] - 1
            remaining_steps -= 1

    return current_town + 1

# Read input
N, K = map(int, input().split())
A = list(map(int, input().split()))

# Find destination town
result = find_teleporter_destination(N, K, A)
print(result)
