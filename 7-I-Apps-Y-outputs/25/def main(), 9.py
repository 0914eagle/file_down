
def main():
    # input
    inp = [int(i) for i in input().split()]
    # get the heights of the two towers
    tower_heights = inp[-2:]
    # get the heights of the six boxes
    box_heights = inp[:-2]
    # sort the heights of the boxes
    box_heights.sort(reverse=True)
    # get the heights of the boxes in the first tower
    first_tower = box_heights[:3]
    # get the heights of the boxes in the second tower
    second_tower = box_heights[3:]
    # print the heights of the boxes in the first tower
    print(*first_tower)
    # print the heights of the boxes in the second tower
    print(*second_tower)

