
def find_destination_town(N, K, A):
    visited = [False] * N
    current_town = 0
    
    while K > 0 and not visited[current_town]:
        visited[current_town] = True
        current_town = A[current_town] - 1
        K -= 1
    
    if K == 0:
        return current_town + 1
    
    cycle_length = visited.index(True) - visited.index(False)
    K %= cycle_length
    
    current_town = 0
    while K > 0:
        current_town = A[current_town] - 1
        K -= 1
    
    return current_town + 1

# Read input
N, K = map(int, input().split())
A = list(map(int, input().split()))

# Call the function and print the result
print(find_destination_town(N, K, A))
