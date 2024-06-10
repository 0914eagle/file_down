
import math

def solve(roost, hiding_spots):
    hiding_spots.sort(key=lambda spot: math.sqrt((roost[0] - spot[0])**2 + (roost[1] - spot[1])**2))

    min_distance = 0
    current_hiding_spots = 0
    for spot in hiding_spots:
        if current_hiding_spots == 2:
            current_hiding_spots = 0
            continue

        distance = math.sqrt((roost[0] - spot[0])**2 + (roost[1] - spot[1])**2)
        min_distance += distance
        current_hiding_spots += 1

    return min_distance


if __name__ == "__main__":
    roost = tuple(map(float, input().split()))
    N = int(input())
    hiding_spots = [tuple(map(float, input().split())) for _ in range(N)]
    print(solve(roost, hiding_spots))

