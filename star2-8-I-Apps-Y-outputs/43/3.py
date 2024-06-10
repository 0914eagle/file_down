
def min_button_presses(floors, start, goal, up, down):
    if up == 0:
        return abs(goal - start)

    if start == goal:
        return 0
    
    if start > goal:
        if start - goal <= down:
            return start - goal
        return "use the stairs"
    
    if goal - start <= up:
        return goal - start
    
    return "use the stairs"
    
floors, start, goal, up, down = map(int, input().split())
print(min_button_presses(floors, start, goal, up, down))

