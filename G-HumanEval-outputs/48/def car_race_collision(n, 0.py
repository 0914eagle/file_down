
def car_race_collision(n: int):
    # For each pair of cars, there will be a collision
    # The number of collisions is the same as the number of pairs
    return n * (n - 1) // 2
