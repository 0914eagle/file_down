
def find_min_pushes(f,s,g,u,d):
    if g > f:
        return "use the stairs"
    pushes = 0
    current_floor = s
    while current_floor != g:
        if current_floor + u > g:
            current_floor -= d
            pushes += 1
        else:
            current_floor += u
            pushes += 1
    return pushes

f,s,g,u,d = map(int,input().split())
print(find_min_pushes(f,s,g,u,d))

