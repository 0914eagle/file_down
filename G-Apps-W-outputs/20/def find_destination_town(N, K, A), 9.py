
def find_destination_town(N, K, A):
    visited = [False] * N
    current_town = 0

    for _ in range(min(K, N)):
        if visited[current_town]:
            loop_start = current_town
            loop_length = 0
            while True:
                loop_length += 1
                current_town = A[current_town] - 1
                if current_town == loop_start:
                    break
            remaining_steps = K - min(K, N)
            remaining_steps %= loop_length
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
result = find_destination_town(N, K, A)
print(result)
