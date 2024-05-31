
def teleporter_town(N, K, A):
    visited = [False] * N
    current_town = 0
    cycle_start_town = 0
    cycle_length = 0
    
    for _ in range(K):
        if visited[current_town]:
            cycle_start_town = current_town
            cycle_length = 0
            break
        visited[current_town] = True
        current_town = A[current_town] - 1
        cycle_length += 1
    
    if cycle_length == 0:
        return current_town + 1
    
    remaining_steps = (K - cycle_start_town) % cycle_length
    while remaining_steps > 0:
        current_town = A[current_town] - 1
        remaining_steps -= 1
    
    return current_town + 1

# Read input
N, K = map(int, input().split())
A = list(map(int, input().split()))

# Call function and print output
print(teleporter_town(N, K, A))
