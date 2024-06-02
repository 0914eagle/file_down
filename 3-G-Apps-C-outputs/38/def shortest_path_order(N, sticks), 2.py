
import heapq

def shortest_path_order(N, sticks):
    # Create a list of tuples where each tuple represents a stick with its label and the distance to the x-axis
    stick_distances = [(i+1, min(stick[1], stick[3])) for i, stick in enumerate(sticks)]
    
    # Sort the sticks based on their distance to the x-axis
    stick_distances.sort(key=lambda x: x[1])
    
    # Extract the labels of the sticks in the order they need to be taken off the table
    order = [stick[0] for stick in stick_distances]
    
    return order

# Input processing
N = int(input())
sticks = []
for _ in range(N):
    x1, y1, x2, y2 = map(int, input().split())
    sticks.append((x1, y1, x2, y2))

# Call the function and print the output
order = shortest_path_order(N, sticks)
print(*order)
