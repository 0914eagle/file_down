
def can_hit_all_targets(N, targets):
    targets = sorted(targets, key=lambda target: target[0])
    
    if N <= 2:
        return "success"

    for i in range(N-1):
        if i == 0 or i == N-2:
            line1 = [targets[0], targets[i+1]]
            remaining_targets = targets[i+2:]
        else:
            line1 = [targets[0], targets[i+1]]
            line2 = [targets[i+1], targets[N-1]]
            remaining_targets = targets[i+2:N-1]

        if all(on_line(line1, target) for target in remaining_targets):
            return "success"

    return "failure"

def on_line(line, target):
    x1, y1 = line[0]
    x2, y2 = line[1]
    x3, y3 = target

    return (y3 - y1) * (x2 - x1) == (y2 - y1) * (x3 - x1)

# Read input
N = int(input())
targets = [tuple(map(int, input().split())) for _ in range(N)]

# Call the function and output the result
print(can_hit_all_targets(N, targets))
