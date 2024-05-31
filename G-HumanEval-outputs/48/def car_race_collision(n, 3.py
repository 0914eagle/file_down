
def car_race_collision(n: int):
    # Number of collisions is equal to the number of pairs of cars
    return n * (n - 1) // 2
