
import sys
import heapq

def calculate_safety_factor(N, M, R, cars):
    INF = float('inf')
    dp = [[INF for _ in range(R+1)] for _ in range(N)]
    dp[0][0] = 0

    pq = [(0, 0, 0)]  # (safety_factor, lane, distance)
    heapq.heapify(pq)

    while pq:
        sf, lane, dist = heapq.heappop(pq)

        if lane == N - 1:
            return sf

        if dp[lane][dist] < sf:
            continue

        for dl in [-1, 1]:
            next_lane = lane + dl

            if 0 <= next_lane < N:
                for car_lane, car_length, car_dist in cars[next_lane]:
                    if car_dist > dist + car_length:
                        new_sf = max(sf, (car_dist - car_length - dist) / 2)
                        if new_sf < dp[next_lane][car_dist]:
                            dp[next_lane][car_dist] = new_sf
                            heapq.heappush(pq, (new_sf, next_lane, car_dist))

    return "Impossible"

# Read input
N, M, R = map(int, input().split())
cars = [[] for _ in range(N)]
for _ in range(M):
    lane, car_length, car_dist = map(int, input().split())
    cars[lane].append((lane, car_length, car_dist))

# Call the function and print the result
result = calculate_safety_factor(N, M, R, cars)
print(result)
