
n = int(input())
cars = list(map(int, input().split()))

def get_min_moves(cars):
    min_moves = 0
    sorted_cars = sorted(cars)
    for car, sorted_car in zip(cars, sorted_cars):
        if car != sorted_car:
            min_moves += 1
    return min_moves

print(get_min_moves(cars))

