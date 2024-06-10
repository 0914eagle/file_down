
import sys

def solve(N, M, K, buildings):
    
    total_noise = 0
    noise = [0] * M # noise level of each building
    empty_count = 0 # number of times the management has emptied a building
    for i in range(N):
        building = buildings[i] - 1 # label of the building, starting from 0
        noise[building] += 1 # increase the noise level of the building
        total_noise += noise[building]
        if empty_count < K and noise[building] >= M: # the management can empty the building
            total_noise -= M * (noise[building] // M) # subtract the noise level of the building after emptying it
            noise[building] %= M # reset the noise level of the building
            empty_count += 1
    return total_noise
if __name__ == '__main__':
    N, M, K = map(int, input().split())
    buildings = []
    for _ in range(N):
        buildings.append(int(input()))
    total_noise = solve(N, M, K, buildings)
    print(total_noise)

