
def max_safety_factor(N, M, R, cars):
    def get_closest_distance(pos, lane):
        closest_distance = float('inf')
        for car_lane, car_length, car_pos in cars:
            if lane == car_lane:
                if car_pos + car_length >= pos:
                    closest_distance = min(closest_distance, car_pos - pos - car_length)
        return closest_distance

    acm_lane, acm_length, acm_pos = cars[0]
    if acm_lane != 0:
        return "Impossible"

    max_safety_factor = 0
    for pos in range(R + acm_length, R + 1):
        closest_distance = min(get_closest_distance(pos, N - 1), get_closest_distance(pos, N - 2))
        max_safety_factor = max(max_safety_factor, closest_distance)

    return max_safety_factor

# Input parsing
N, M, R = map(int, input().split())
cars = [list(map(int, input().split())) for _ in range(M)]

result = max_safety_factor(N, M, R, cars)
print(result)
