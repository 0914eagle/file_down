
def main():
    # input
    heights = list(map(int, input().split()))
    towers = list(map(int, input().split()))

    # processing
    # sort heights
    heights.sort()

    # sort towers
    towers.sort()

    # get towers
    tower_1 = heights[:3]
    tower_2 = heights[-3:]

    # output
    print(*tower_1)
    print(*tower_2)


