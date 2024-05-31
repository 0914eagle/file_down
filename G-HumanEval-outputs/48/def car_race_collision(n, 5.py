
def car_race_collision(n: int):
    # Each pair of cars will collide once, so the total number of collisions is the same as the number of pairs
    return n * (n - 1) // 2
