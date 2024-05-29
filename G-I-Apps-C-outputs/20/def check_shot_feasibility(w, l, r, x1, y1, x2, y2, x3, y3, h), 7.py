
import math

def check_shot_feasibility(w, l, r, x1, y1, x2, y2, x3, y3, h):
    # Calculate the center coordinates of the holes
    hole1_x = 0
    hole1_y = l
    hole2_x = w
    hole2_y = l
    
    # Calculate the center coordinates of the cue ball
    cue_x = w / 2
    cue_y = l - h
    
    # Calculate the vector from cue ball to ball 1 at time of collision
    v1_x = x1 - cue_x
    v1_y = y1 - cue_y
    
    # Calculate the new direction vector for ball 1 after collision with cue ball
    new_v1_x = v1_x
    new_v1_y = v1_y
    
    # Calculate the vector from ball 1 to ball 3 at time of collision
    v3_x = x3 - x1
    v3_y = y3 - y1
    
    # Calculate the new direction vector for ball 3 after collision with ball 1
    new_v3_x = v3_x
    new_v3_y = v3_y
    
    # Calculate the angle between the x-axis and the direction vector from ball 1 to ball 3
    angle = math.degrees(math.atan2(new_v3_y, new_v3_x))
    
    # Calculate the distance d to place the cue ball on the dashed line
    d = x1 - r
    
    # Check if the shot is possible
    if x2 < d + r or y2 < r:
        return "impossible"
    
    return format(d, '.2f') + " " + format(angle, '.2f')

# Read input
w, l = map(int, input().split())
r, x1, y1, x2, y2, x3, y3, h = map(int, input().split())

# Check shot feasibility
result = check_shot_feasibility(w, l, r, x1, y1, x2, y2, x3, y3, h)

# Output result
print(result)
```

