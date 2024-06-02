
def count_good_observatories(N, M, elevations, roads):
    good_observatories = set(range(1, N+1))
    
    for i in range(M):
        A, B = roads[i]
        if elevations[A-1] <= elevations[B-1]:
            good_observatories.discard(A)
        if elevations[B-1] <= elevations[A-1]:
            good_observatories.discard(B)
    
    return len(good_observatories)

# Input processing
N, M = map(int, input().split())
elevations = list(map(int, input().split()))
roads = [list(map(int, input().split())) for _ in range(M)]

# Call the function and print the result
result = count_good_observatories(N, M, elevations, roads)
print(result)
