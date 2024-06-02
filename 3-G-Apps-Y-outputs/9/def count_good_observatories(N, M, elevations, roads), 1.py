
def count_good_observatories(N, M, elevations, roads):
    good_obs = set(range(1, N+1))
    
    for a, b in roads:
        if elevations[a-1] <= elevations[b-1]:
            good_obs.discard(a)
        if elevations[b-1] <= elevations[a-1]:
            good_obs.discard(b)
    
    return len(good_obs)

# Input processing
N, M = map(int, input().split())
elevations = list(map(int, input().split()))
roads = [tuple(map(int, input().split())) for _ in range(M)]

# Call the function and print the result
result = count_good_observatories(N, M, elevations, roads)
print(result)
