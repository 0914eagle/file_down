
def car_race_collision(n: int):
    # Since the cars are moving at the same speed, the collisions will happen when the two sets of cars meet.
    # The number of collisions will be equal to the number of pairs of cars meeting each other.
    # Therefore, the number of collisions is n choose 2, which is equal to n*(n-1)/2.

    return n * (n - 1) // 2
