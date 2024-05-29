
import math

def is_possible(w, l, r, x1, y1, x2, y2, x3, y3, h):
    def distance(x1, y1, x2, y2):
        return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
    
    def angle(x1, y1, x2, y2):
        return math.degrees(math.atan2(y2 - y1, x2 - x1))
    
    def reflection(ball, cue_ball, hole):
        v_cue = (math.cos(math.radians(cue_ball['angle'])),
                 math.sin(math.radians(cue_ball['angle'])))
        v_target = (hole['center'][0] - ball['center'][0],
                    hole['center'][1] - ball['center'][1])
        dot = v_target[0] * v_cue[0] + v_target[1] * v_cue[1]
        reflection = (v_cue[0] - 2 * dot * v_target[0], v_cue[1] - 2 * dot * v_target[1])
        return reflection

    def check_collision(cue_ball, ball, radius, hole):
        d = distance(cue_ball['center'][0], cue_ball['center'][1],
                     ball['center'][0], ball['center'][1])
        if d < 2 * radius:
            reflection_vector = reflection(ball, cue_ball, hole)
            ball['angle'] = angle(0, 0, reflection_vector[0], reflection_vector[1]) % 360
            return True
        return False
    
    balls = [
        {'center': (x1, y1), 'angle': None},
        {'center': (x2, y2), 'angle': None},
        {'center': (x3, y3), 'angle': None}
    ]
    
    cue_ball = {'center': (w/2, h), 'angle': None}
    holes = [{'center': (0, l), 'radius': r}, {'center': (w, l), 'radius': r}]
    
    if not all(ball['center'][1] >= h and ball['center'][1] <= l for ball in balls):
        return "impossible"
    
    if not all(check_collision(cue_ball, ball, r, hole) for ball, hole in zip(balls, holes)):
        return "impossible"
    
    return round(distance(w/2, h, balls[0]['center'][0], balls[0]['center'][1]), 2), \
           round(angle(w/2, h, balls[0]['center'][0], balls[0]['center'][1]), 2)

# Input parsing
w, l = map(int, input().split())
r, x1, y1, x2, y2, x3, y3, h = map(int, input().split())

# Check if trick shot is possible
result = is_possible(w, l, r, x1, y1, x2, y2, x3, y3, h)

if result == "impossible":
    print("impossible")
else:
    print(*result)
```

