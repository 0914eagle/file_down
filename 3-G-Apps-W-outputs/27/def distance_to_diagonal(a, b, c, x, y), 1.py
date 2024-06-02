
import math

def distance_to_diagonal(a, b, c, x, y):
    if a == 0:
        return abs(x + c)
    if b == 0:
        return abs(y + c)
    
    # Calculate the projection of point (x, y) onto the diagonal avenue
    x_proj = (b*(b*x - a*y) - a*c) / (a**2 + b**2)
    y_proj = (a*(-b*x + a*y) - b*c) / (a**2 + b**2)
    
    # Calculate the distance between the point and its projection on the avenue
    dist_to_diagonal = math.sqrt((x - x_proj)**2 + (y - y_proj)**2)
    
    # Calculate the distance from point A to its projection on the avenue and from there to point B
    dist_A_to_diagonal = abs(a*x + b*y + c) / math.sqrt(a**2 + b**2)
    dist_B_to_diagonal = abs(a*x_proj + b*y_proj + c) / math.sqrt(a**2 + b**2)
    
    return dist_A_to_diagonal + dist_to_diagonal + dist_B_to_diagonal

# Input
a, b, c = map(int, input().split())
x1, y1, x2, y2 = map(int, input().split())

# Output
result = distance_to_diagonal(a, b, c, x1, y1) + distance_to_diagonal(a, b, c, x2, y2)
print("{:.10f}".format(result))
