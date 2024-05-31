
def find_destination_town(N, K, A):
    visited = [False] * N
    current_town = 0

    for _ in range(K):
        if visited[current_town]:
            cycle_start = current_town
            cycle_length = 0

            while not visited[current_town]:
                visited[current_town] = True
                current_town = A[current_town] - 1
                cycle_length += 1
            
            remaining_steps = K % cycle_length

            current_town = cycle_start
            for _ in range(remaining_steps):
                current_town = A[current_town] - 1
            break

        visited[current_town] = True
        current_town = A[current_town] - 1

    return current_town + 1

# Read input
N, K = map(int, input().split())
A = list(map(int, input().split()))

# Find the destination town
destination_town = find_destination_town(N, K, A)
print(destination_town)
