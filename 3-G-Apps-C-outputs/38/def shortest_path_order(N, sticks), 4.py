
import heapq

def shortest_path_order(N, sticks):
    # Create a list of tuples where each tuple contains the stick label and the distance to the x-axis
    stick_distances = []
    for i, stick in enumerate(sticks):
        x1, y1, x2, y2 = stick
        distance = min(y1, y2)  # Distance is the minimum y-coordinate of the stick
        stick_distances.append((distance, i+1))  # Add 1 to stick label to start from 1

    # Sort the sticks based on their distances to the x-axis
    stick_distances.sort()

    # Extract the stick labels in the order they need to be taken off the table
    order = [stick[1] for stick in stick_distances]

    return order

# Input
N = int(input())
sticks = []
for _ in range(N):
    x1, y1, x2, y2 = map(int, input().split())
    sticks.append((x1, y1, x2, y2))

# Get the order of stick movements
order = shortest_path_order(N, sticks)

# Output
print(*order)
