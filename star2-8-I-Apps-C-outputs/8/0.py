
n = int(input())
cars = list(map(int, input().split()))

def solve(cars):
    min_actions = 0
    i = 0
    while i < n:
        if cars[i] != i + 1:
            cars[cars[i] - 1] = cars[i]
            cars[i] = i + 1
            min_actions += 1
        else:
            i += 1
    
    return min_actions

print(solve(cars))

