
def find_final_town(N, K, A):
    visited = [False] * N
    current_town = 0
    cycle_start = -1
    cycle_length = 0

    for _ in range(K):
        if visited[current_town]:
            cycle_start = current_town
            break
        visited[current_town] = True
        current_town = A[current_town] - 1

    if cycle_start != -1:  # If a cycle is found
        for i in range(K):
            if current_town == cycle_start:
                cycle_length = i
                break
            current_town = A[current_town] - 1

    if cycle_start == -1:
        return current_town + 1
    else:
        remaining_steps = (K - cycle_start) % cycle_length
        for _ in range(remaining_steps):
            current_town = A[current_town] - 1
        return current_town + 1

# Reading input from stdin
N, K = map(int, input().split())
A = list(map(int, input().split()))

# Finding the final town the king will be in
result = find_final_town(N, K, A)
print(result)
