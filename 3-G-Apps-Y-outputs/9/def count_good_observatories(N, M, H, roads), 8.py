
def count_good_observatories(N, M, H, roads):
    good_obs = set(range(1, N+1))
    
    for a, b in roads:
        if H[a-1] <= H[b-1]:
            good_obs.discard(a)
        if H[b-1] <= H[a-1]:
            good_obs.discard(b)
    
    return len(good_obs)

# Read input
N, M = map(int, input().split())
H = list(map(int, input().split()))
roads = [tuple(map(int, input().split())) for _ in range(M)]

# Call the function and print the result
result = count_good_observatories(N, M, H, roads)
print(result)
