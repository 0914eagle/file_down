
def max_points(n, arr):
    points = 0
    stack = []
    
    for i in range(n):
        while stack and stack[-1] > arr[i]:
            current = stack.pop()
            if not stack:
                points += current
            else:
                points += min(current, stack[-1])
        stack.append(arr[i])
    
    while len(stack) > 1:
        points += stack.pop()
    
    return points

# Input
n = int(input())
arr = list(map(int, input().split()))

# Output
print(max_points(n, arr))
