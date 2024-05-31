
def calculate_safety_factor(N, M, R, cars):
    cars = sorted(cars, key=lambda x: (x[0], x[2]))  # Sort cars by lane number and distance from start
    lane_cars = [[] for _ in range(N)]  # Cars in each lane
    for car in cars:
        lane_cars[car[0]].append(car)

    safety_factor = float("inf")
    for i in range(len(lane_cars[0])):
        acm_car = lane_cars[0][i]
        for j in range(len(lane_cars[N-1])):
            target_car = lane_cars[N-1][j]
            if acm_car[2] + acm_car[1] + R <= target_car[2]:  # Check if there is enough space to switch lanes
                safety_factor = min(safety_factor, target_car[2] - acm_car[2] - acm_car[1])

    if safety_factor == float("inf"):
        print("Impossible")
    else:
        print("{:.6f}".format(safety_factor))

# Sample Input Parsing
N, M, R = map(int, input().split())
cars = [list(map(int, input().split())) for _ in range(M)]

# Call the function with the provided inputs
calculate_safety_factor(N, M, R, cars)
